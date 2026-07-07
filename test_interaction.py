import json
import os
from dotenv import load_dotenv
load_dotenv()

from modules import agent_logic

api_key = os.environ.get("GEMINI_API_KEY", "")
if not api_key:
    print("Error: GEMINI_API_KEY not found in environment!")
    exit(1)

# Simular la historia de la imagen
history = [
    {
        "role": "assistant",
        "content": "¡Hola! Soy tu consultor experto en automatización de Total Opportunity y optimización de campañas de marketing digital.\n\nMi misión es guiarte paso a paso para recolectar y validar todos los inputs del modelo de Total Opportunity a lo largo de 5 fases.\n\nPara empezar, ¿cuál es el **Tipo de Campañas** que tiene tu cliente actualmente sobre la cual se hará el total opportunity? Cuéntame también qué rango de meses planeas proyectar."
    },
    {
        "role": "user",
        "content": "2 Pmax y sem y tiene 1 año de historia"
    },
    {
        "role": "assistant",
        "content": "Entendido. Tienes 2 campañas PMax y SEM con 1 año de historia. Ahora, por favor, proporciona la inversión y conversión mensualizada para cada una de estas campañas, idealmente de los últimos 6 meses."
    },
    {
        "role": "user",
        "content": "40000 1000 25000 600"
    }
]

inputs = json.loads(json.dumps(agent_logic.INITIAL_INPUTS))

print("Llamando a Gemini con historia...")
result = agent_logic.call_gemini(
    api_key=api_key,
    model_name="gemini-2.5-flash-lite",
    conversation_history=history,
    current_inputs=inputs
)

print("\n--- RESULTADO RETORNADO ---")
print(json.dumps(result, indent=2, ensure_ascii=False))
