import streamlit as st
from PIL import Image
import io

st.set_page_config(layout="wide", page_title="CLOTCHITO AI - Analista de Identidad")

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

    # Bloque de Identidad con descripción física
    identity_block = ""
    if preserve_face:
        # Aquí inyectamos los rasgos físicos que tú describas
        identity_block = f"Character description: ({traits}). High-fidelity identity preservation, preserving EXACT facial features, bone structure, and identity. DO NOT change the face. "

    tech_prompt = f"Hyper-realistic studio portrait, {identity_block}"
    tech_prompt += f"the person is {base_prompt}, "
    tech_prompt += f"{optica_map.get(lens, '')}, "
    tech_prompt += f"{luz_map.get(lighting, '')}, "
    tech_prompt += f"8k resolution, photorealistic, masterwork, highly detailed skin textures, sharp focus on eyes"
    
    return tech_prompt

# --- INTERFAZ ---
st.title("📸 CLOTCHITO AI - Identity Master")

col_settings, col_main = st.columns([1, 2])

with col_settings:
    st.subheader("⚙️ Control Técnico")
    realismo = st.slider("Realismo", 0, 100, 95)
    optica = st.selectbox("Lente", ["85mm", "35mm", "24mm"])
    iluminacion = st.selectbox("Luz", ["Cinemática", "Estudio", "Natural"])
    preservar = st.checkbox("FORZAR IDENTIDAD", value=True)

with col_main:
    uploaded_image = st.file_uploader("1. Sube la foto", type=["jpg", "png", "jpeg"])
    
    # NUEVO CAMPO: Para que la IA "sepa" cómo es la persona
    user_traits = st.text_area("2. Describe sus rasgos físicos (Ej: mujer latina, cabello ondulado negro, ojos cafés)", placeholder="Esto ayuda a la IA a no inventar rasgos...")
    
    user_prompt = st.text_input("3. Acción o Escenario (Ej: en la playa con ropa de verano)")
    
    if st.button("Generar Prompt con Descripción"):
        if user_traits and user_prompt:
            final_p = build_production_prompt(user_prompt, user_traits, realismo, optica, iluminacion, preservar)
            st.code(final_p, language='text')
        else:
            st.error("Socio, necesito los rasgos y la acción para que el prompt sea perfecto.")
