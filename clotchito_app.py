import streamlit as st
import random

# Configuración de la página
st.set_page_config(page_title="CLOTCHITO AI - Prompt Engine", page_icon="📸", layout="wide")

# Estilo personalizado para un look oscuro y pro
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stTextInput textarea { color: #ffffff !important; }
    .stChatMessage { border-radius: 15px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DE CLOTCHITO (EL SECRET SAUCE) ---
def build_pro_prompt(base_idea, realism_level, lens_type, lighting):
    # Diccionarios técnicos de la vieja escuela
    specs = {
        "85mm": "shot on 85mm lens, f/1.8, creamy bokeh, sharp focus on eyes, portrait photography",
        "35mm": "35mm wide angle, street photography style, deep depth of field, f/8",
        "Macro": "macro lens, extreme close-up, microscopic detail, f/2.8",
    }
    
    lighting_styles = {
        "Cinemática": "cinematic lighting, dramatic shadows, teal and orange color grading, volumetric fog",
        "Estudio": "high-key studio lighting, softbox, professional photography, clean background",
        "Natural": "golden hour, natural sunlight, soft shadows, outdoor lighting",
    }

    # Construcción del prompt con esteroides
    prompt = f"Hyper-realistic photo of {base_idea}, {specs[lens_type]}, {lighting_styles[lighting]}, "
    prompt += "extremely detailed skin textures, 8k resolution, photorealistic, masterwork, "
    
    if realism_level > 80:
        prompt += "unreal engine 5 render style, ray tracing, subsurface scattering, highly sophisticated detail, sharp textures, "
    
    prompt += "highly detailed, digital production, professional color grading --ar 16:9 --v 6.0"
    
    return prompt

# --- INTERFAZ ---
st.title("📸 CLOTCHITO AI")
st.subheader("Tu socio de confianza en producción digital")

# Barra lateral - Controles de Realismo
with st.sidebar:
    st.header("🎚️ Ajustes de Producción")
    realism = st.slider("Nivel de Realismo (Hiperrealismo)", 0, 100, 90)
    lens = st.selectbox("Óptica (Lente)", ["85mm", "35mm", "Macro"])
    light = st.selectbox("Esquema de Iluminación", ["Cinemática", "Estudio", "Natural"])
    st.divider()
    st.info("Socio, estos ajustes inyectan metadatos técnicos al prompt para engañar al ojo.")

# Historial del chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes previos
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input del usuario
if prompt_input := st.chat_input("¿Qué tienes en mente, socio? (Ej: Un cyberpunk en un callejón)"):
    # Agregar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": prompt_input})
    with st.chat_message("user"):
        st.markdown(prompt_input)

    # Lógica de respuesta de CLOTCHITO
    with st.chat_message("assistant"):
        with st.spinner("Procesando en el laboratorio..."):
            pro_prompt = build_pro_prompt(prompt_input, realism, lens, light)
            response = f"Aquí tienes el setup, socio. He ajustado la óptica a **{lens}** y la luz es **{light}**. Pégalo en Midjourney o Stable Diffusion:\n\n`{pro_prompt}`"
            st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})