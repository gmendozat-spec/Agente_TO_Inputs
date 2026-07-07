import json
import os
from dotenv import load_dotenv
load_dotenv()

from modules import agent_logic

api_key = os.environ.get("GEMINI_API_KEY", "")

# Historial acumulado e inputs
history = []
inputs = json.loads(json.dumps(agent_logic.INITIAL_INPUTS))

# Mensajes del usuario del chat
user_messages = [
    "2 Pmax y sem y tiene 1 año de historia",
    "40000 1000 25000 600",
    "5000 y 100 para pmax y 7000 y 90 sem",
    "Inversión PMAX: 1000 Conversión PMAX: 100 Inversión SEM: 2000 Conversión SEM: 200"
]

# Inicialización con el primer mensaje del asistente
history.append({
    "role": "assistant",
    "content": "¡Hola! Soy tu consultor experto en automatización de Total Opportunity y optimización de campañas de marketing digital.\n\nMi misión es guiarte paso a paso para recolectar y validar todos los inputs del modelo de Total Opportunity a lo largo de 5 fases.\n\nPara empezar, ¿cuál es el **Tipo de Campañas** que tiene tu cliente actualmente sobre la cual se hará el total opportunity? Cuéntame también qué rango de meses planeas proyectar."
})

for i, user_msg in enumerate(user_messages):
    print(f"\n================ TURN {i+1} ================")
    print(f"User: {user_msg}")
    history.append({"role": "user", "content": user_msg})
    
    print("Calling Gemini...")
    result = agent_logic.call_gemini(
        api_key=api_key,
        model_name="gemini-2.5-flash-lite",
        conversation_history=history,
        current_inputs=inputs
    )
    
    response = result.get("chat_response")
    inputs = result.get("extracted_inputs", inputs)
    
    print(f"Assistant: {response}")
    print("State Inputs:")
    print(json.dumps(inputs["phase_1_historico"], indent=2, ensure_ascii=False))
    
    # Añadir respuesta del asistente para el siguiente turno
    history.append({"role": "assistant", "content": response})
