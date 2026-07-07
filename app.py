import streamlit as st
import json
import pandas as pd
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Importar módulos locales
from modules import styles, agent_logic

# Configuración inicial de página Streamlit
st.set_page_config(
    page_title="AI Agent | Total Opportunity Inputs",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Aplicar estilos CSS corporativos oficiales de Google
styles.apply_custom_styles()

# Inicializar estados de la sesión
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {
            "role": "assistant",
            "content": "¡Hola! Soy tu consultor experto en automatización de Total Opportunity y optimización de campañas de marketing digital.\n\nMi misión es guiarte paso a paso para recolectar y validar todos los inputs del modelo de Total Opportunity a lo largo de 5 fases.\n\nPara empezar, ¿cuál es el **Tipo de Campañas** que tiene tu cliente actualmente sobre la cual se hará el total opportunity? Cuéntame también qué rango de meses planeas proyectar."
        }
    ]

if "extracted_inputs" not in st.session_state or any(k not in st.session_state.extracted_inputs for k in agent_logic.INITIAL_INPUTS):
    st.session_state.extracted_inputs = json.loads(json.dumps(agent_logic.INITIAL_INPUTS))

# Obtener API Key de las variables de entorno (.env)
api_key = os.environ.get("GEMINI_API_KEY", "")

# -------------------------------------------------------------------------
# PANEL LATERAL (SIDEBAR): CONFIGURACIÓN DE MODELO Y CHECKLIST
# -------------------------------------------------------------------------
with st.sidebar:
    st.markdown("## 🤖 **Configuración del Agente**")
    st.markdown("<span style='color: #5F6368;'>Motor de Inteligencia Artificial</span>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Selección de modelo
    model_name = st.selectbox(
        "Modelo de Gemini:",
        ["gemini-2.5-flash-lite"],
        index=0,
        help="El modelo '2.5-flash-lite' es ideal por su balance entre velocidad y precisión."
    )
    
    st.markdown("---")
    st.markdown("### 📋 Progreso de Recolección")
    
    # Mapeo de nombres para mostrar de las 5 fases
    module_names = {
        "phase_1_historico": "1. Datos Históricos del Cliente",
        "phase_2_bau": "2. Crecimiento BAU (Connect)",
        "phase_3_optimizations": "3. Crecimiento por Optimizaciones",
        "phase_4_elasticidad": "4. Curvas de Elasticidad",
        "phase_5_consideration_awareness": "5. Consideración & Awareness"
    }
    
    # Dibujar checklist en base al estado actual
    for mod_key, mod_name in module_names.items():
        status = st.session_state.extracted_inputs[mod_key]["status"]
        
        # Verificar si está activo o completado
        if status == "completed":
            bg_class = "completed"
            status_text = "✅ Completado"
        elif status == "active":
            bg_class = "active"
            status_text = "🔵 En Progreso"
        else:
            # Si tiene algún valor pero no está completo del todo
            # O simplemente es pending
            bg_class = "pending"
            status_text = "⚪ Pendiente"
            
        # Contar campos llenos
        fields = st.session_state.extracted_inputs[mod_key]
        total_fields = len([k for k in fields.keys() if k != 'status'])
        filled_fields = len([k for k, v in fields.items() if k != 'status' and v is not None])
        
        st.markdown(f"""
        <div class="progress-box {bg_class}">
            <div class="progress-title">{mod_name}</div>
            <div class="progress-status">{status_text} ({filled_fields}/{total_fields} campos)</div>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    
    # Botón para resetear todo
    if st.button("Resetear Conversación & Inputs", use_container_width=True):
        st.session_state.chat_history = [
            {
                "role": "assistant",
                "content": "¡Hola! Soy tu consultor experto en automatización de Total Opportunity y optimización de campañas de marketing digital.\n\nMi misión es guiarte paso a paso para recolectar y validar todos los inputs del modelo de Total Opportunity a lo largo de 5 fases.\n\nPara empezar, ¿cuál es el **Tipo de Campañas** que tiene tu cliente actualmente sobre la cual se hará el total opportunity? Cuéntame también qué rango de meses planeas proyectar."
            }
        ]
        st.session_state.extracted_inputs = json.loads(json.dumps(agent_logic.INITIAL_INPUTS))
        st.rerun()

# -------------------------------------------------------------------------
# CUERPO PRINCIPAL
# -------------------------------------------------------------------------
st.markdown("<h1>🤖 Consultor Experto de <span class='gradient-text'>Total Opportunity</span></h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #5F6368; font-size: 1.1rem;'>Conversa con el agente experto para recolectar y validar los datos requeridos por las 5 fases core.</p>", unsafe_allow_html=True)

tab1, tab2 = st.tabs([
    "💬 Asistente Conversacional",
    "📁 Inputs Compilados"
])

# =========================================================================
# PESTAÑA 1: ASISTENTE CONVERSACIONAL (CHAT)
# =========================================================================
with tab1:
    # Si la API Key no está configurada, mostrar una advertencia clara
    if not api_key:
        st.error("⚠️ **Falta la API Key de Gemini:** Configura la variable `GEMINI_API_KEY` en el archivo `.env` de la aplicación para poder iniciar la conversación.")
    
    # Contenedor para la historia del chat
    chat_container = st.container()
    
    # Dibujar historial
    with chat_container:
        for message in st.session_state.chat_history:
            with st.chat_message(message["role"]):
                st.write(message["content"])
                
    # Entrada de chat
    user_input = st.chat_input("Escribe tu respuesta o consulta aquí...")
    
    if user_input:
        if not api_key:
            st.error("No se puede enviar el mensaje sin una API Key configurada en el archivo `.env`.")
        else:
            # Mostrar el mensaje del usuario de inmediato
            with chat_container:
                with st.chat_message("user"):
                    st.write(user_input)
            
            # Guardar en el historial
            st.session_state.chat_history.append({"role": "user", "content": user_input})
            
            # Llamar a la API de Gemini con indicador de carga
            with st.spinner("El consultor está analizando tus datos..."):
                result = agent_logic.call_gemini(
                    api_key=api_key,
                    model_name=model_name,
                    conversation_history=st.session_state.chat_history,
                    current_inputs=st.session_state.extracted_inputs
                )
            
            # Guardar la respuesta de texto del chatbot
            chat_response = result.get("chat_response", "Lo siento, tuve un problema para procesar tu consulta.")
            st.session_state.chat_history.append({"role": "assistant", "content": chat_response})
            
            # Actualizar los inputs extraídos en el estado de sesión
            if "extracted_inputs" in result:
                st.session_state.extracted_inputs = result["extracted_inputs"]
                
            # Recargar la página para actualizar el checklist y el chat
            st.rerun()

# =========================================================================
# PESTAÑA 2: INPUTS COMPILADOS (COMPILER FORMAT)
# =========================================================================
with tab2:
    st.markdown("### 📁 Compilación de Parámetros de Total Opportunity")
    st.caption("Esta tabla consolida los datos extraídos por el agente en tiempo real. Cuando todas las fases estén completas, podrás copiar este formato para ingresarlo en el modelo financiero.")
    
    # Crear un DataFrame limpio con los datos recolectados
    flat_data = []
    for mod_key, mod_name in module_names.items():
        module_data = st.session_state.extracted_inputs[mod_key]
        for field_name, field_value in module_data.items():
            if field_name != "status":
                flat_data.append({
                    "Fase / Módulo": mod_name,
                    "Parámetro / Input": field_name.replace("_", " ").title(),
                    "Valor Extraído": str(field_value) if field_value is not None else "⚠️ Pendiente",
                    "Estado": "✅ Validado" if field_value is not None else "❌ Faltante"
                })
                
    df_inputs = pd.DataFrame(flat_data)
    
    # Mostrar tabla interactiva
    st.dataframe(df_inputs, use_container_width=True)
    
    st.markdown("---")
    st.markdown("#### 📜 Formato JSON Listo para Copiar")
    st.caption("Formato estructurado del estado de recolección:")
    
    st.code(json.dumps(st.session_state.extracted_inputs, indent=2, ensure_ascii=False), language="json")
    
    # Botón para descargar el JSON
    json_str = json.dumps(st.session_state.extracted_inputs, indent=2, ensure_ascii=False)
    st.download_button(
        label="📥 Descargar Inputs (JSON)",
        data=json_str,
        file_name="total_opportunity_extracted_inputs.json",
        mime="application/json"
    )
