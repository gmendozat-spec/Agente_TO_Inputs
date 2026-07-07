# 🤖 Agente Conversacional Experto en Total Opportunity (TO)

Esta aplicación implementa un agente conversacional experto en guiar a los consultores y clientes para encontrar y validar los inputs exactos requeridos por las 6 metodologías del cálculo de **Total Opportunity (TO)**.

El agente está construido utilizando **Google Gemini** y **Streamlit**, siguiendo la documentación metodológica oficial del proceso.

---

## 🌟 Características

1. **Agente Conversacional Experto (Gemini API):**
   - Configurado con instrucciones de comportamiento detalladas del manual de entrenamiento.
   - Aplica validaciones estrictas en tiempo real:
     - **Crecimiento BAU (Módulo 1):** Valida tasas históricas y sugiere defaults de la industria financiera (4% en conversiones, 2% en CPA/CPC).
     - **Auditoría de Headroom (Módulo 3):** Exige mantener la optimización del CPA estrictamente en 0%.
     - **Configuración de Alcance (Módulo 6):** Exige el uso de la población total (sin filtros de nicho demográfico) con un benchmark de CPR de 0.09 y objetivo del 60%.
2. **Checklist de Progreso Interactivo:**
   - La barra lateral izquierda muestra el progreso en tiempo real de cada uno de los 6 módulos a medida que chateas con el agente.
3. **Compilador y Exportador de Formato Final:**
   - La pestaña **Inputs Compilados** recopila la estructura de datos tabulada y genera un formato JSON limpio listo para copiar y pegar en la calculadora definitiva.

---

## 💻 Ejecución Local

### 1. Activar Entorno Virtual e Instalar Dependencias
```bash
# Crear entorno virtual (si no existe)
python3 -m venv venv

# Activar entorno
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt --index-url https://pypi.org/simple
```

### 2. Configurar la API Key de Gemini
Puedes configurar tu API Key creando un archivo `.env` en este directorio:
```env
GEMINI_API_KEY=tu_api_key_aqui
```
O también puedes introducirla directamente en la barra lateral de la interfaz web.

### 3. Levantar la Aplicación
```bash
python3 -m streamlit run app.py --server.port=8502
```

La app estará disponible en: 👉 **[http://localhost:8502](http://localhost:8502)**

---

## 🐳 Despliegue con Docker

Puedes construir y ejecutar el contenedor en cualquier plataforma compatible (Cloud Run, ECS, Kubernetes):

```bash
# 1. Construir la imagen Docker
docker build -t agente-to-app .

# 2. Correr el contenedor mapeando el puerto 8502
docker run -d -p 8502:8501 -e GEMINI_API_KEY="tu_api_key" --name agente-to-container agente-to-app
```

---

## ☁️ Despliegue en Google Cloud Run

Para desplegar en Google Cloud Run de manera rápida:

```bash
# 1. Construir y subir la imagen a Google Artifact Registry
gcloud builds submit --tag gcr.io/TU_PROJECT_ID/agente-to-app

# 2. Desplegar el servicio en Cloud Run
gcloud run deploy agente-to-service \
    --image gcr.io/TU_PROJECT_ID/agente-to-app \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated \
    --set-env-vars="GEMINI_API_KEY=tu_api_key"
```
