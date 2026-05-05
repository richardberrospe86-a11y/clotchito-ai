import streamlit as st
from PIL import Image
import io

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(layout="wide", page_title="CLOTCHITO AI - Identity Master")

# --- LÓGICA DE INYECCIÓN DE METADATOS Y RASGOS ---
def build_production_prompt(base_prompt, realism_level, lens, lighting, preserve_face):
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

    # Bloque de Identidad (Tu Llave Maestra)
    identity_block = ""
    if preserve_face:
        identity_block = "preserving EXACT facial features, bone structure, and identity, 100% identity preservation, DO NOT change the face, "

    # Construcción final del prompt
    tech_prompt = f"Hyper-realistic studio portrait of the person in the reference image, {identity_block}"
    tech_prompt += f"transformed into {base_prompt}, "
    tech_prompt += f"{optica_map.get(lens, '')}, "
    tech_prompt += f"{luz_map.get(lighting, '')}, "
    tech_prompt += f"8k resolution, photorealistic, masterwork, highly detailed skin textures, sharp focus on eyes"
    
    return tech_prompt

# --- INTERFAZ ---
st.markdown("<h1 style='text-align: center;'>📸 CLOTCHITO AI - Identity Master</h1>", unsafe_allow_html=True)
st.write("---")

col_settings, col_main = st.columns([1, 2])

with col_settings:
    st.subheader("⚙️ Control de Producción")
    realismo = st.slider("Nivel de Realismo", 0, 100, 95)
    optica = st.selectbox("Óptica (Lente)", ["85mm", "35mm", "24mm"])
    iluminacion = st.selectbox("Esquema de Iluminación", ["Cinemática", "Estudio", "Natural"])
    
    # NUEVA OPCIÓN: Preservar Rostro
    preservar = st.checkbox("MANTENER RASGOS FACIALES (Identidad)", value=True)
    
    st.info("Socio, con el check activo, el prompt forzará a la IA a no deformar la cara de la foto.")

with col_main:
    uploaded_image = st.file_uploader("1. Sube la foto del personaje", type=["jpg", "png", "jpeg"])
    
    if uploaded_image:
        st.image(Image.open(uploaded_image), width=300)
    
    user_prompt = st.text_input("2. ¿En qué lo transformamos? (Ej: Un guerrero Inka, un busto de mármol)", key="input")
    
    if st.button("Generar Prompt Maestro", type="primary"):
        if uploaded_image and user_prompt:
            final_p = build_production_prompt(user_prompt, realismo, optica, iluminacion, preservar)
            st.success("✅ Prompt de Identidad Generado")
            st.code(final_p, language='text')
            st.warning("Copia este prompt y úsalo con tu imagen en Midjourney o Stable Diffusion.")
        else:
            st.error("Socio, falta la imagen o la descripción.")
