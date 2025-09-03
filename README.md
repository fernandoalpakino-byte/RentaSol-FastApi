# 🍽️ RentaSol FastAPI

Sistema de gestión de restaurantes y reservas de mesas desarrollado con FastAPI y PostgreSQL.

## 🚀 Características

- **Gestión de Usuarios**: Propietarios de restaurantes y clientes
- **Administración de Restaurantes**: Información, horarios, ubicación GPS
- **Sistema de Menús**: Categorías, platillos y precios
- **Gestión de Mesas**: Capacidad, estado y códigos QR
- **Sistema de Reservas**: Fechas, montos y estados
- **Redes Sociales**: Enlaces a Facebook e Instagram
- **Configuración Segura**: Variables de entorno para credenciales

## 🛠️ Tecnologías

- **Backend**: FastAPI (Python)
- **Base de Datos**: PostgreSQL
- **ORM**: SQLModel (SQLAlchemy + Pydantic)
- **Autenticación**: JWT con bcrypt
- **Configuración**: Variables de entorno con Pydantic Settings

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

### 5. Configurar variables de entorno

#### Opción A: Generar automáticamente (Recomendado)
```bash
python create_env.py
```

#### Opción B: Crear manualmente
```bash
# Copiar el archivo de ejemplo
cp env.example .env

# Editar el archivo .env con tus credenciales
nano .env  # o usar tu editor preferido
```

### 6. Configurar base de datos
- Crear base de datos PostgreSQL: `c-labs-demo`
- Usuario: `postgres`
- Contraseña: `123456789` (o la que configures en .env)
- Puerto: `5432`

### 7. Ejecutar la aplicación
```bash
python main.py
```

La API estará disponible en: `http://localhost:8000`

## 🔐 Configuración de Variables de Entorno

### Variables Principales

| Variable | Descripción | Valor por Defecto |
|----------|-------------|-------------------|
| `DB_HOST` | Host de la base de datos | `localhost` |
| `DB_PORT` | Puerto de la base de datos | `5432` |
| `DB_NAME` | Nombre de la base de datos | `c-labs-demo` |
| `DB_USERNAME` | Usuario de la base de datos | `postgres` |
| `DB_PASSWORD` | Contraseña de la base de datos | `123456789` |
| `SECRET_KEY` | Clave secreta para JWT | Generada automáticamente |
| `ALGORITHM` | Algoritmo de encriptación | `HS256` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Expiración de tokens | `30` |
| `ENVIRONMENT` | Entorno de ejecución | `development` |
| `DEBUG` | Modo debug | `true` |

### Configuración por Entorno

#### Desarrollo
```env
ENVIRONMENT=development
DEBUG=true
LOG_LEVEL=DEBUG
```

#### Producción
```env
ENVIRONMENT=production
DEBUG=false
LOG_LEVEL=WARNING
SECRET_KEY=tu_clave_secreta_muy_segura
```

### Seguridad

⚠️ **Importante**: 
- Nunca subas el archivo `.env` al repositorio
- Cambia las contraseñas por defecto
- Usa claves secretas seguras en producción
- El archivo `.env` ya está en `.gitignore`

## 📚 Documentación de la API

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
- **Health Check**: `http://localhost:8000/health`
- **Configuración**: `http://localhost:8000/config` (solo en desarrollo)

## 🗄️ Estructura del Proyecto

```
RentaSol-FastApi/
├── app/
│   ├── __init__.py
│   ├── models/           # Modelos de base de datos
│   ├── schemas/          # Esquemas de Pydantic
│   ├── api/              # Endpoints de la API
│   │   ├── routers/      # Rutas de la API
│   │   └── deps/         # Dependencias (auth)
│   ├── core/             # Configuración central
│   ├── database/         # Configuración de BD y semillas
│   ├── services/         # Lógica de negocio
│   ├── repositories/     # Acceso a datos
│   └── utils/            # Utilidades (JWT, seguridad)
├── main.py               # Archivo principal
├── create_env.py         # Script para generar .env
├── env.example           # Ejemplo de variables de entorno
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

### Autenticación
- `POST /auth/login` - Login de usuarios

### Usuarios
- `POST /usuarios` - Crear usuario
- `GET /usuarios` - Listar usuarios

### Restaurantes
- `POST /restaurantes` - Crear restaurante (propietario)
- `GET /restaurantes` - Listar restaurantes

### Cartas
- `POST /cartas` - Crear carta (propietario)
- `GET /cartas` - Listar cartas

### Platillos
- `POST /platillos` - Crear platillo (Admin)
- `GET /platillos` - Listar platillos
- `PUT /platillos/{id}` - Actualizar platillo
- `DELETE /platillos/{id}` - Eliminar platillo

### Mesas
- `POST /mesas` - Crear mesa (propietario)
- `GET /mesas` - Listar mesas

### Reservas
- `POST /restaurantes/{id}/reservas` - Crear reserva (autenticado)

### Sistema
- `GET /` - Información de la API
- `GET /health` - Estado de la API
- `GET /config` - Configuración (solo desarrollo)

## 🚧 Próximas Funcionalidades

- [ ] CRUD completo para todas las entidades
- [ ] Validaciones avanzadas
- [ ] Tests unitarios
- [ ] Documentación completa
- [ ] Sistema de pagos
- [ ] Notificaciones push
- [ ] Docker y Docker Compose
- [ ] CI/CD pipeline

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
