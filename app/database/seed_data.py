from datetime import datetime, time
from sqlmodel import Session, select
from typing import List
import uuid

# Importar modelos desde la nueva estructura
from app.models import (
    Usuario, 
    Restaurante, 
    CategoriaCarta, 
    Carta, 
    CategoriaPlatillos, 
    Platillo, 
    Mesa, 
    Redes, 
    MesasReservadas
)
from app.database.database import engine

def create_seed_data():
    """Crear datos de prueba en la base de datos"""
    with Session(engine) as session:
        # Verificar si ya existe data para no duplicar
        existing_users = session.exec(select(Usuario)).first()
        if existing_users:
            print("✅ Ya existe data en la base de datos. Saltando creación de semillas.")
            return

        print("🌱 Creando datos de prueba...")

        # 1. Crear Usuarios
        usuarios = [
            Usuario(
                nombre="Juan",
                apellido="Pérez",
                ruc="20100066661",
                correo="juan@restaurant.com",
                telefono="+51987654321",
                password="password123",  # En producción, usar hash!
                tipousuario="propietario"
            ),
            Usuario(
                nombre="María",
                apellido="Gómez",
                ruc="20100066662",
                correo="maria@restaurant.com",
                telefono="+51987654322",
                password="password123",
                tipousuario="propietario"
            ),
            Usuario(
                nombre="Carlos",
                apellido="López",
                ruc=None,
                correo="carlos@cliente.com",
                telefono="+51987654323",
                password="password123",
                tipousuario="cliente"
            )
        ]

        for usuario in usuarios:
            session.add(usuario)
        
        session.commit()
        session.refresh(usuarios[0])
        session.refresh(usuarios[1])

        # 2. Crear Restaurantes
        restaurantes = [
            Restaurante(
                nombrelocal="La Parrilla del Juan",
                descripcion="Carnes a la parrilla y comida criolla",
                telefono="014567890",
                direccion="Av. Siempre Viva 123, Lima",
                horadeapertura=time(12, 0),
                horadecierre=time(22, 0),
                latitud=-12.0464,
                longitud=-77.0428,
                logo="https://ejemplo.com/logo1.jpg",
                idusuario=usuarios[0].idusuario
            ),
            Restaurante(
                nombrelocal="María's Sushi Bar",
                descripcion="Sushi fresco y comida japonesa",
                telefono="014567891",
                direccion="Av. Javier Prado 456, Lima",
                horadeapertura=time(11, 30),
                horadecierre=time(23, 0),
                latitud=-12.0670,
                longitud=-77.0335,
                logo="https://ejemplo.com/logo2.jpg",
                idusuario=usuarios[1].idusuario
            )
        ]

        for restaurante in restaurantes:
            session.add(restaurante)
        
        session.commit()
        session.refresh(restaurantes[0])
        session.refresh(restaurantes[1])

        # 3. Crear Redes Sociales
        redes = [
            Redes(
                idrestaurante=restaurantes[0].idrestaurante,
                facebookurl="https://facebook.com/laparrilla",
                instagramurl="https://instagram.com/laparrilla"
            ),
            Redes(
                idrestaurante=restaurantes[1].idrestaurante,
                facebookurl="https://facebook.com/mariassushi",
                instagramurl="https://instagram.com/mariassushi"
            )
        ]

        for red in redes:
            session.add(red)

        # 4. Crear Categorías de Carta
        categorias_carta = [
            CategoriaCarta(
                nombrecategoria="Menú Principal",
                descripcioncategoria="Platos principales del restaurante",
                idrestaurante=restaurantes[0].idrestaurante
            ),
            CategoriaCarta(
                nombrecategoria="Bebidas",
                descripcioncategoria="Bebidas y refrescos",
                idrestaurante=restaurantes[0].idrestaurante
            ),
            CategoriaCarta(
                nombrecategoria="Sushi Rolls",
                descripcioncategoria="Variedad de rolls japoneses",
                idrestaurante=restaurantes[1].idrestaurante
            )
        ]

        for categoria in categorias_carta:
            session.add(categoria)
        
        session.commit()
        session.refresh(categorias_carta[0])
        session.refresh(categorias_carta[1])
        session.refresh(categorias_carta[2])

        # 5. Crear Cartas
        cartas = [
            Carta(
                nombrecarta="Carta Principal",
                idcategoriacarta=categorias_carta[0].idcategoria,
                idrestaurante=restaurantes[0].idrestaurante
            ),
            Carta(
                nombrecarta="Carta de Bebidas",
                idcategoriacarta=categorias_carta[1].idcategoria,
                idrestaurante=restaurantes[0].idrestaurante
            ),
            Carta(
                nombrecarta="Carta de Sushi",
                idcategoriacarta=categorias_carta[2].idcategoria,
                idrestaurante=restaurantes[1].idrestaurante
            )
        ]

        for carta in cartas:
            session.add(carta)
        
        session.commit()
        session.refresh(cartas[0])
        session.refresh(cartas[1])
        session.refresh(cartas[2])

        # 6. Crear Categorías de Platillos
        categorias_platillos = [
            CategoriaPlatillos(
                nombrecategoria="Carnes",
                descripcion="Platos de carne"
            ),
            CategoriaPlatillos(
                nombrecategoria="Pescados",
                descripcion="Platos de pescado"
            ),
            CategoriaPlatillos(
                nombrecategoria="Sushi",
                descripcion="Rolls y piezas de sushi"
            )
        ]

        for categoria in categorias_platillos:
            session.add(categoria)
        
        session.commit()
        session.refresh(categorias_platillos[0])
        session.refresh(categorias_platillos[1])
        session.refresh(categorias_platillos[2])

        # 7. Crear Platillos
        platillos = [
            Platillo(
                nombre="Lomo Saltado",
                descripcion="Lomo de res salteado con cebolla, tomate y papas fritas",
                precio=35.00,
                imageurl="https://ejemplo.com/lomo.jpg",
                moneda="pen",
                idcategoria=categorias_platillos[0].idcategoria,
                idcarta=cartas[0].idcarta
            ),
            Platillo(
                nombre="Ceviche Mixto",
                descripcion="Ceviche de pescado y mariscos",
                precio=40.00,
                imageurl="https://ejemplo.com/ceviche.jpg",
                moneda="pen",
                idcategoria=categorias_platillos[1].idcategoria,
                idcarta=cartas[0].idcarta
            ),
            Platillo(
                nombre="California Roll",
                descripcion="Roll con cangrejo, palta y pepino",
                precio=25.00,
                imageurl="https://ejemplo.com/california.jpg",
                moneda="pen",
                idcategoria=categorias_platillos[2].idcategoria,
                idcarta=cartas[2].idcarta
            )
        ]

        for platillo in platillos:
            session.add(platillo)

        # 8. Crear Mesas
        mesas = []
        for i in range(1, 6):
            mesa = Mesa(
                numeromesa=i,
                capacidad=4 if i <= 3 else 6,
                estado="disponible",
                qrcode=f"QR_MESA_{i}_{restaurantes[0].idrestaurante[:8]}",
                restauranteid=restaurantes[0].idrestaurante
            )
            mesas.append(mesa)
            session.add(mesa)

        for i in range(1, 4):
            mesa = Mesa(
                numeromesa=i,
                capacidad=2,
                estado="disponible",
                qrcode=f"QR_MESA_{i}_{restaurantes[1].idrestaurante[:8]}",
                restauranteid=restaurantes[1].idrestaurante
            )
            mesas.append(mesa)
            session.add(mesa)

        # 9. Crear Reservas
        reservas = [
            MesasReservadas(
                idrestaurante=restaurantes[0].idrestaurante,
                idusuario=usuarios[2].idusuario,
                fechadereserva=datetime(2024, 1, 15, 19, 0),
                montoabonado=50.00,
                estado="confirmada"
            ),
            MesasReservadas(
                idrestaurante=restaurantes[1].idrestaurante,
                idusuario=usuarios[2].idusuario,
                fechadereserva=datetime(2024, 1, 16, 20, 0),
                montoabonado=30.00,
                estado="pendiente"
            )
        ]

        for reserva in reservas:
            session.add(reserva)

        # Commit final
        session.commit()
        print("✅ Datos de prueba creados exitosamente!")
        print(f"   - {len(usuarios)} usuarios")
        print(f"   - {len(restaurantes)} restaurantes")
        print(f"   - {len(platillos)} platillos")
        print(f"   - {len(mesas)} mesas")
        print(f"   - {len(reservas)} reservas")

if __name__ == "__main__":
    create_seed_data()
