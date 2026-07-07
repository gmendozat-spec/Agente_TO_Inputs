# Dockerfile para producción (Google Cloud Run / AWS / Docker)
FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias del sistema requeridas para Streamlit y salud
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Copiar archivos de requerimientos e instalar dependencias usando el repositorio público
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --index-url https://pypi.org/simple

# Copiar el resto de los archivos del proyecto
COPY . .

# Exponer el puerto estándar de Streamlit
EXPOSE 8501

# Comprobar la salud del contenedor
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Ejecutar Streamlit al iniciar el contenedor
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
