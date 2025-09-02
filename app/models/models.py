from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime, time
import uuid

def generate_uuid() -> str:
    """Generar un UUID único para los IDs"""
    return str(uuid.uuid4())

class Usuario(SQLModel, table=True):
    __tablename__ = "usuario"

    idusuario: str = Field(default_factory=generate_uuid, primary_key=True)
    nombre: str = Field(max_length=100, nullable=False)
    apellido: str = Field(max_length=100, nullable=False)
    ruc: Optional[str] = Field(default=None, max_length=15)
    correo: str = Field(max_length=100, nullable=False, unique=True)
    telefono: str = Field(max_length=100, nullable=False)
    password: str = Field(max_length=300, nullable=False)
    fechacreacion: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    tipousuario: str = Field(max_length=20, nullable=False)

    # Relaciones
    restaurantes: List["Restaurante"] = Relationship(back_populates="usuario")
    reservas: List["MesasReservadas"] = Relationship(back_populates="usuario")

class Restaurante(SQLModel, table=True):
    __tablename__ = "restaurante"

    idrestaurante: str = Field(default_factory=generate_uuid, primary_key=True)
    nombrelocal: str = Field(max_length=100, nullable=False)
    descripcion: str = Field(nullable=False)
    telefono: str = Field(max_length=15, nullable=False)
    direccion: str = Field(max_length=100, nullable=False)
    horadeapertura: time = Field(nullable=False)
    horadecierre: time = Field(nullable=False)
    latitud: Optional[float] = Field(default=None)
    longitud: Optional[float] = Field(default=None)
    logo: Optional[str] = Field(default=None)
    createdat: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    idusuario: str = Field(foreign_key="usuario.idusuario", nullable=False)

    # Relaciones
    usuario: Usuario = Relationship(back_populates="restaurantes")
    cartas: List["Carta"] = Relationship(back_populates="restaurante")
    redes: Optional["Redes"] = Relationship(back_populates="restaurante")
    mesas: List["Mesa"] = Relationship(back_populates="restaurante")
    reservas: List["MesasReservadas"] = Relationship(back_populates="restaurante")

class Carta(SQLModel, table=True):
    __tablename__ = "carta"

    idcarta: str = Field(default_factory=generate_uuid, primary_key=True)
    nombrecarta: str = Field(max_length=100, nullable=False)
    idcategoriacarta: str = Field(foreign_key="categoria_carta.idcategoria", nullable=False)
    idrestaurante: str = Field(foreign_key="restaurante.idrestaurante", nullable=False)

    # Relaciones
    restaurante: Restaurante = Relationship(back_populates="cartas")
    platillos: List["Platillo"] = Relationship(back_populates="carta")

class Mesa(SQLModel, table=True):
    __tablename__ = "mesas"

    idmesa: str = Field(default_factory=generate_uuid, primary_key=True)
    numeromesa: int = Field(nullable=False)
    capacidad: int = Field(nullable=False)
    estado: str = Field(max_length=15, nullable=False)
    qrcode: str = Field(max_length=100, nullable=False)
    restauranteid: str = Field(foreign_key="restaurante.idrestaurante", nullable=False)

    # Relaciones
    restaurante: Restaurante = Relationship(back_populates="mesas")

class Redes(SQLModel, table=True):
    __tablename__ = "redes"

    idrestaurante: str = Field(foreign_key="restaurante.idrestaurante", primary_key=True)
    facebookurl: Optional[str] = Field(default=None, max_length=200)
    instagramurl: Optional[str] = Field(default=None, max_length=200)

    # Relaciones
    restaurante: Restaurante = Relationship(back_populates="redes")

class CategoriaPlatillos(SQLModel, table=True):
    __tablename__ = "categoria_platillos"

    idcategoria: str = Field(default_factory=generate_uuid, primary_key=True)
    nombrecategoria: str = Field(max_length=100, nullable=False)
    descripcion: str = Field(max_length=100, nullable=False)

    # Relaciones
    platillos: List["Platillo"] = Relationship(back_populates="categoria_obj")

class CategoriaCarta(SQLModel, table=True):
    __tablename__ = "categoria_carta"

    idcategoria: str = Field(default_factory=generate_uuid, primary_key=True)
    nombrecategoria: str = Field(max_length=100, nullable=False)
    descripcioncategoria: str = Field(max_length=100, nullable=False)
    idrestaurante: str = Field(foreign_key="restaurante.idrestaurante", nullable=False)

class Platillo(SQLModel, table=True):
    __tablename__ = "platillos"

    idplatillo: str = Field(default_factory=generate_uuid, primary_key=True)
    idcategoria: str = Field(foreign_key="categoria_platillos.idcategoria", nullable=False)
    nombre: str = Field(max_length=100, nullable=False)
    descripcion: str = Field(nullable=False)
    precio: float = Field(nullable=False)
    imageurl: str = Field(nullable=False)
    moneda: str = Field(max_length=10, nullable=False, default="pen")
    idcarta: str = Field(foreign_key="carta.idcarta", nullable=False)

    # Relaciones
    categoria_obj: CategoriaPlatillos = Relationship(back_populates="platillos")
    carta: Carta = Relationship(back_populates="platillos")

class MesasReservadas(SQLModel, table=True):
    __tablename__ = "mesas_reservadas"

    idreserva: str = Field(default_factory=generate_uuid, primary_key=True)
    idrestaurante: str = Field(foreign_key="restaurante.idrestaurante", nullable=False)
    idusuario: str = Field(foreign_key="usuario.idusuario", nullable=False)
    fechadereserva: datetime = Field(nullable=False)
    montoabonado: float = Field(nullable=False)
    estado: str = Field(max_length=20, nullable=False, default="pendiente")

    # Relaciones
    usuario: Usuario = Relationship(back_populates="reservas")
    restaurante: Restaurante = Relationship(back_populates="reservas")
