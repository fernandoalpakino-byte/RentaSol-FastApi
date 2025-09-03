import os
from typing import Optional
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Cargar variables de entorno desde archivo .env
load_dotenv()

class DatabaseSettings(BaseModel):
    """Configuración de la base de datos"""
    host: str = Field(default="localhost", description="Host de la base de datos")
    port: int = Field(default=5432, description="Puerto de la base de datos")
    database: str = Field(default="c-labs-demo", description="Nombre de la base de datos")
    username: str = Field(default="postgres", description="Usuario de la base de datos")
    password: str = Field(default="123456789", description="Contraseña de la base de datos")
    
    @property
    def url(self) -> str:
        """Genera la URL de conexión a la base de datos"""
        return f"postgresql+psycopg2://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"

class JWTSettings(BaseModel):
    """Configuración de JWT"""
    secret_key: str = Field(default="change-me", description="Clave secreta para JWT")
    algorithm: str = Field(default="HS256", description="Algoritmo de encriptación")
    access_token_expire_minutes: int = Field(default=30, description="Tiempo de expiración del token en minutos")

class AppSettings(BaseModel):
    """Configuración general de la aplicación"""
    app_name: str = Field(default="RentaSol FastAPI", description="Nombre de la aplicación")
    app_version: str = Field(default="1.0.0", description="Versión de la aplicación")
    debug: bool = Field(default=False, description="Modo debug")
    environment: str = Field(default="development", description="Entorno de ejecución")

class Settings(BaseSettings):
    """Configuración principal de la aplicación"""
    
    # Configuraciones específicas
    database: DatabaseSettings = DatabaseSettings()
    jwt: JWTSettings = JWTSettings()
    app: AppSettings = AppSettings()
    
    # Variables de entorno individuales (para compatibilidad)
    secret_key: str = Field(default="change-me", env="SECRET_KEY")
    algorithm: str = Field(default="HS256", env="ALGORITHM")
    access_token_expire_minutes: int = Field(default=30, env="ACCESS_TOKEN_EXPIRE_MINUTES")
    
    # Base de datos (para compatibilidad con código existente)
    database_url: str = Field(default="", env="DATABASE_URL")
    
    # Variables individuales de base de datos
    db_host: str = Field(default="localhost", env="DB_HOST")
    db_port: int = Field(default=5432, env="DB_PORT")
    db_name: str = Field(default="c-labs-demo", env="DB_NAME")
    db_username: str = Field(default="postgres", env="DB_USERNAME")
    db_password: str = Field(default="123456789", env="DB_PASSWORD")
    
    # Configuración de la aplicación
    app_name: str = Field(default="RentaSol FastAPI", env="APP_NAME")
    app_version: str = Field(default="1.0.0", env="APP_VERSION")
    environment: str = Field(default="development", env="ENVIRONMENT")
    debug: bool = Field(default=False, env="DEBUG")
    
    # Configuración del servidor
    port: int = Field(default=8000, env="PORT")
    host: str = Field(default="0.0.0.0", env="HOST")
    
    # Configuración de logging
    log_level: str = Field(default="INFO", env="LOG_LEVEL")
    
    # Configuración de seguridad
    max_file_size: int = Field(default=10485760, env="MAX_FILE_SIZE")  # 10MB
    allowed_origins: str = Field(default="http://localhost:3000,http://localhost:8080", env="ALLOWED_ORIGINS")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Actualizar la configuración de la base de datos con las variables individuales
        self.database.host = self.db_host
        self.database.port = self.db_port
        self.database.database = self.db_name
        self.database.username = self.db_username
        self.database.password = self.db_password
        
        # Actualizar la configuración de JWT
        self.jwt.secret_key = self.secret_key
        self.jwt.algorithm = self.algorithm
        self.jwt.access_token_expire_minutes = self.access_token_expire_minutes
        
        # Actualizar la configuración de la aplicación
        self.app.app_name = self.app_name
        self.app.app_version = self.app_version
        self.app.environment = self.environment
        self.app.debug = self.debug

# Instancia global de configuración
settings = Settings()

# Función para obtener la URL de la base de datos
def get_database_url() -> str:
    """Obtiene la URL de la base de datos, priorizando DATABASE_URL si está definida"""
    if settings.database_url:
        return settings.database_url
    return settings.database.url
