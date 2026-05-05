import streamlit as st
from PIL import Image
import io

# --- CONFIGURACIÓN ---
st.set_page_config(layout="wide", page_title="CLOTCHITO AI - Identity Master")

def build_production_prompt(base_prompt, traits, realism_level, lens, lighting, preserve_face):
    optica_map = {
        "85mm": "shot on 85mm lens, f/1.8, creamy bokeh, portrait photography",
        "35mm": "shot on 35mm lens, f/5.6, street photography style",
        "24mm": "shot on 24mm wide-angle lens, landscape photography"
    }
    
    luz_map = {
        "Cinemática": "cinematic lighting, dramatic shadows, volumetric fog, teal and orange color grading",
        "Estudio": "studio lighting, softbox, high key, professional photography",
        "Natural": "natural daylight, golden hour, soft shadows"
    }

    identity_block = ""
    if preserve_face:
        # Inyección de los rasgos que tú vas a describir
        identity_block = f"Character physical description: ({traits}). High-fidelity identity preservation, preserving EXACT facial features, bone structure, and identity. DO NOT change the face. "

    tech_prompt = f"Hyper-realistic studio portrait, {identity_block}"
    tech_prompt += f"the person is {base_prompt}, "
    tech_prompt += f"{optica_map.get(lens, '')}, "
    tech_prompt += f"{luz_map.get(lighting, '')}, "
    tech_prompt += f"8k resolution, photorealistic, masterwork, highly detailed skin textures, sharp focus on eyes"
    
    return tech_prompt

# --- INTERFAZ ---
st.markdown("<h1 style='text-align: center;'>📸 CLOTCHITO AI - Identity Master</h1>", unsafe_allow_html=True)
st.write("---")

col_settings, col_main = st.columns([1, 2])

with col_settings:
    st.subheader("⚙️ Control Técnico")
    realismo = st.slider("Realismo", 0, 100, 95)
    optica = st.selectbox("Lente", ["85mm", "35mm", "24mm"])
    iluminacion = st.selectbox("Luz", ["Cinemática", "Estudio", "Natural"])
    preservar = st.checkbox("MANTENER IDENTIDAD", value=True)

with col_main:
    uploaded_image = st.file_uploader("1. Sube la foto base", type=["jpg", "png", "jpeg"])
    
    # IMPORTANTE: Aquí escribes los rasgos de la persona de la foto
    user_traits = st.text_area("2. Rasgos físicos (Ej: mujer, cabello largo negro, ojos verdes, tez clara)", placeholder="Describe a la persona de la foto aquí...")
    
    user_prompt = st.text_input("3. Acción o Escenario (Ej: caminando en la playa con ropa de verano)")
    
    if st.button("Generar Prompt de Identidad", type="primary"):
        if user_traits and user_prompt:
            final_p = build_production_prompt(user_prompt, user_traits, realismo, optica, iluminacion, preservar)
            st.success("✅ Prompt Maestro Generado")
            st.code(final_p, language='text')
        else:
            st.error("Socio, necesito los rasgos (cuadro 2) y la acción (cuadro 3).")
