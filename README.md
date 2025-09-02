# 🍽️ RentaSol FastAPI

Sistema de gestión de restaurantes y reservas de mesas desarrollado con FastAPI y PostgreSQL.

## 🚀 Características

- **Gestión de Usuarios**: Propietarios de restaurantes y clientes
- **Administración de Restaurantes**: Información, horarios, ubicación GPS
- **Sistema de Menús**: Categorías, platillos y precios
- **Gestión de Mesas**: Capacidad, estado y códigos QR
- **Sistema de Reservas**: Fechas, montos y estados
- **Redes Sociales**: Enlaces a Facebook e Instagram

## 🛠️ Tecnologías

- **Backend**: FastAPI (Python)
- **Base de Datos**: PostgreSQL
- **ORM**: SQLModel (SQLAlchemy + Pydantic)
- **Autenticación**: Sistema básico de usuarios

## 📋 Requisitos Previos

- Python 3.8+
- PostgreSQL 12+
- pip (gestor de paquetes de Python)

## 🔧 Instalación

### 1. Clonar el repositorio
```bash
git clone <url-del-repositorio>
cd RentaSol-FastApi
```

### 2. Crear entorno virtual
```bash
python -m venv renta-sol-fast-api-env
```

### 3. Activar entorno virtual
```bash
# Windows
renta-sol-fast-api-env\Scripts\activate

# Linux/Mac
source renta-sol-fast-api-env/bin/activate
```

### 4. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 5. Configurar base de datos
- Crear base de datos PostgreSQL: `c-labs-demo`
- Usuario: `postgres`
- Contraseña: `123456789`
- Puerto: `5432`

### 6. Ejecutar la aplicación
```bash
python main.py
```

La API estará disponible en: `http://localhost:8000`

## 📚 Documentación de la API

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🗄️ Estructura del Proyecto

```
RentaSol-FastApi/
├── app/
│   ├── __init__.py
│   ├── models/           # Modelos de base de datos
│   ├── schemas/          # Esquemas de Pydantic
│   ├── api/              # Endpoints de la API
│   ├── core/             # Configuración central
│   ├── database/         # Configuración de BD y semillas
│   ├── services/         # Lógica de negocio
│   └── utils/            # Utilidades
├── main.py               # Archivo principal
├── requirements.txt       # Dependencias
└── README.md
```

## 🌱 Datos de Prueba

La aplicación incluye datos de prueba automáticos:
- 3 usuarios (2 propietarios, 1 cliente)
- 2 restaurantes (parrilla y sushi)
- Categorías de platillos
- Menús y platillos de ejemplo
- Mesas con códigos QR
- Reservas de ejemplo

## 🔌 Endpoints Principales

- `GET /` - Información de la API
- `GET /health` - Estado de la API
- `POST /usuarios` - Crear usuario
- `GET /usuarios` - Listar usuarios

## 🚧 Próximas Funcionalidades

- [ ] CRUD completo para todas las entidades
- [ ] Sistema de autenticación JWT
- [ ] Validaciones avanzadas
- [ ] Tests unitarios
- [ ] Documentación completa
- [ ] Sistema de pagos
- [ ] Notificaciones push

## 🤝 Contribuir

1. Fork el proyecto
2. Crear una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abrir un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.

## 📞 Soporte

Para soporte técnico, contacta al equipo de desarrollo.
