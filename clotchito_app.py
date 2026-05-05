import streamlit as st
from PIL import Image # Necesario para manejar imágenes
import io

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(layout="wide", page_title="CLOTCHITO AI - Img2Img Production")

# --- LÓGICA DE INYECCIÓN DE METADATOS ---
def build_production_prompt(base_prompt, realism_level, lens, lighting):
    # Traducciones y lógica técnica
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

    # Construcción del prompt técnico
    tech_prompt = f"Hyper-realistic photo of {base_prompt}"
    
    if realism_level > 70:
        tech_prompt += f", {realism_level}% realism, highly detailed, photorealistic, masterwork"
    
    tech_prompt += f", {optica_map.get(lens, '')}"
    tech_prompt += f", {luz_map.get(lighting, '')}"
    
    # Motor de render y calidad final
    tech_prompt += ", unreal engine 5 render style, ray tracing, 8k resolution, subsurface scattering"
    
    return tech_prompt

# --- INTERFAZ DE USUARIO (UI) ---

# Título y subtítulo
st.markdown("<h1 style='text-align: center;'>📸 CLOTCHITO AI - Img2Img</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2em;'>Tu socio de confianza en producción digital - Modo Imagen</p>", unsafe_allow_html=True)
st.write("---")

# Layout de dos columnas
col_settings, col_main = st.columns([1, 2])

with col_settings:
    st.subheader("⚙️ Ajustes de Producción")
    
    # Slider de Realismo
    realismo = st.slider("Nivel de Realismo (Hiperrealismo)", 0, 100, 90)
    
    # Selector de Óptica
    optica = st.selectbox("Óptica (Lente)", ["85mm", "35mm", "24mm"])
    
    # Selector de Iluminación
    iluminacion = st.selectbox("Esquema de Iluminación", ["Cinemática", "Estudio", "Natural"])
    
    st.info("Socio, estos ajustes se aplicarán como metadatos técnicos para guiar la transformación de la imagen.")

with col_main:
    st.subheader("🛠️ Panel de Creación")
    
    # --- NUEVO: SUBIDOR DE IMAGEN ---
    uploaded_image = st.file_uploader("1. Sube tu imagen base (JPG, PNG)", type=["jpg", "png", "jpeg"])
    
    # Mostrar la imagen subida
    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Imagen Base Subida", use_column_width=True)
        st.success("Imagen cargada correctamente, socio.")
    else:
        st.warning("Sube una imagen para empezar la transformación Img2Img.")

    # --- ENTRADA DE TEXTO ---
    user_prompt = st.text_input("2. ¿Qué transformación quieres aplicar? (Ej: Convertir en estatua de piedra)", key="prompt_input")
    
    # Botón para generar
    generate_btn = st.button("Generar Prompt de Producción", type="primary")

    if generate_btn and user_prompt and uploaded_image:
        # Construir el prompt técnico
        final_prompt = build_production_prompt(user_prompt, realismo, optica, iluminacion)
        
        st.write("---")
        st.success("✅ ¡Aquí tienes el setup Img2Img, socio!")
        st.info(f"Usaremos la imagen subida con la óptica **{optica}** y luz **{iluminacion}**.")
        
        # Mostrar el prompt final en inglés
        st.markdown("**Prompt Técnico Final (para Img2Img):**")
        st.code(final_prompt, language='text')
        
        st.warning("⚠️ Nota: Por ahora, copia este prompt y úsalo junto a tu imagen en Midjourney/Stable Diffusion (modo Img2Img). La conexión directa para procesar la imagen requiere una API de pago.")

    elif generate_btn and not uploaded_image:
        st.error("Socio, necesitas subir una imagen primero.")
    elif generate_btn and not user_prompt:
        st.error("Escribe un prompt para guiar la transformación.")
