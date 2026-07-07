import streamlit as st

def apply_custom_styles():
    """
    Aplica estilos CSS corporativos oficiales de Google con fondo blanco puro (#FFFFFF),
    bordes grises limpios (#DADCE0), texto oscuro (#202124) y la paleta de colores de Google:
    Azul (#4285F4), Rojo (#EA4335), Amarillo (#FBBC04) y Verde (#34A853).
    """
    custom_css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

    /* Fuente global y texto oscuro estilo Google Workspace/Ads */
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
        color: #202124;
    }

    /* Fondo principal blanco puro */
    .stApp {
        background-color: #FFFFFF !important;
    }

    /* Estilo del Sidebar (Gris claro Google) */
    section[data-testid="stSidebar"] {
        background-color: #F8F9FA !important;
        border-right: 1px solid #DADCE0;
    }
    section[data-testid="stSidebar"] .block-container {
        padding-top: 2rem;
    }

    /* Títulos en texto oscuro */
    h1, h2, h3 {
        color: #202124 !important;
        font-weight: 700 !important;
    }
    .gradient-text {
        background: linear-gradient(90deg, #4285F4 0%, #34A853 33%, #FBBC04 66%, #EA4335 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* Estilos de las cajas del Checklist de Progreso */
    .progress-box {
        background-color: #F8F9FA;
        border: 1px solid #DADCE0;
        border-radius: 8px;
        padding: 12px 16px;
        margin-bottom: 10px;
        transition: all 0.2s ease;
    }
    .progress-box.completed {
        border-left: 5px solid #34A853;
        background-color: #E6F4EA;
    }
    .progress-box.pending {
        border-left: 5px solid #F1F3F4;
    }
    .progress-box.active {
        border-left: 5px solid #4285F4;
        background-color: #E8F0FE;
        font-weight: bold;
    }
    .progress-title {
        font-size: 0.9rem;
        font-weight: 600;
        margin-bottom: 4px;
    }
    .progress-status {
        font-size: 0.8rem;
        color: #5F6368;
    }

    /* Botones con estilo Google Blue */
    .stButton > button {
        background: linear-gradient(135deg, #4285F4 0%, #3367D6 100%);
        color: #FFFFFF;
        font-weight: 700;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.5rem;
        box-shadow: 0 2px 8px rgba(66, 133, 244, 0.25);
        transition: all 0.2s ease;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #5B9BFF 0%, #4285F4 100%);
        box-shadow: 0 4px 14px rgba(66, 133, 244, 0.4);
        transform: translateY(-2px);
        color: #FFFFFF;
    }

    /* Caja de formato final compilado */
    .compile-box {
        background-color: #F1F3F4;
        border: 1px solid #DADCE0;
        border-radius: 8px;
        padding: 16px;
        font-family: monospace;
        white-space: pre-wrap;
        color: #202124;
    }

    /* Info boxes */
    .info-box {
        background-color: #E8F0FE;
        border-left: 4px solid #4285F4;
        padding: 14px;
        border-radius: 0 8px 8px 0;
        margin: 10px 0;
        font-size: 0.9rem;
    }
    .warning-box {
        background-color: #FEF7E0;
        border-left: 4px solid #FBBC04;
        padding: 14px;
        border-radius: 0 8px 8px 0;
        margin: 10px 0;
        font-size: 0.9rem;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)
