#!/usr/bin/env python3
"""
Script para crear el archivo .env con la configuración por defecto
"""

import os
import secrets

def generate_secret_key():
    """Genera una clave secreta segura para JWT"""
    return secrets.token_urlsafe(32)

def create_env_file():
    """Crea el archivo .env con la configuración por defecto"""
    
    # Verificar si ya existe el archivo .env
    if os.path.exists('.env'):
        print("⚠️  El archivo .env ya existe. ¿Deseas sobrescribirlo? (y/N): ", end="")
        response = input().strip().lower()
        if response != 'y':
            print("❌ Operación cancelada.")
            return
    
    # Generar clave secreta segura
    secret_key = generate_secret_key()
    
    # Contenido del archivo .env
    env_content = f"""# ========================================
# CONFIGURACIÓN DE LA APLICACIÓN RENTASOL
# ========================================

# ========================================
# CONFIGURACIÓN DE LA BASE DE DATOS
# ========================================

# Opción 1: URL completa de la base de datos (recomendado para producción)
# DATABASE_URL=postgresql+psycopg2://usuario:contraseña@host:puerto/nombre_base_datos

# Opción 2: Configuración individual (recomendado para desarrollo)
DB_HOST=localhost
DB_PORT=5432
DB_NAME=c-labs-demo
DB_USERNAME=postgres
DB_PASSWORD=123456789

# ========================================
# CONFIGURACIÓN DE JWT
# ========================================

# Clave secreta para firmar tokens JWT (¡CAMBIAR EN PRODUCCIÓN!)
SECRET_KEY={secret_key}

# Algoritmo de encriptación para JWT
ALGORITHM=HS256

# Tiempo de expiración del token en minutos
ACCESS_TOKEN_EXPIRE_MINUTES=30

# ========================================
# CONFIGURACIÓN DE LA APLICACIÓN
# ========================================

# Nombre de la aplicación
APP_NAME=RentaSol FastAPI

# Versión de la aplicación
APP_VERSION=1.0.0

# Entorno de ejecución (development, staging, production)
ENVIRONMENT=development

# Modo debug (true/false)
DEBUG=true

# ========================================
# CONFIGURACIÓN ADICIONAL
# ========================================

# Puerto del servidor (opcional, por defecto 8000)
PORT=8000

# Host del servidor (opcional, por defecto 0.0.0.0)
HOST=0.0.0.0

# ========================================
# CONFIGURACIÓN DE LOGGING
# ========================================

# Nivel de logging (DEBUG, INFO, WARNING, ERROR, CRITICAL)
LOG_LEVEL=INFO

# ========================================
# CONFIGURACIÓN DE SEGURIDAD
# ========================================

# Tamaño máximo de archivos subidos (en bytes)
MAX_FILE_SIZE=10485760  # 10MB

# Lista de dominios permitidos para CORS
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8080
"""
    
    # Escribir el archivo .env
    try:
        with open('.env', 'w', encoding='utf-8') as f:
            f.write(env_content)
        print("✅ Archivo .env creado exitosamente!")
        print(f"🔑 Clave secreta generada: {secret_key[:20]}...")
        print("\n📝 Recuerda:")
        print("   - Cambiar la contraseña de la base de datos")
        print("   - Ajustar la configuración según tu entorno")
        print("   - Nunca subir el archivo .env al repositorio")
        
    except Exception as e:
        print(f"❌ Error al crear el archivo .env: {e}")

if __name__ == "__main__":
    print("🚀 Generando archivo .env para RentaSol FastAPI...")
    create_env_file()
