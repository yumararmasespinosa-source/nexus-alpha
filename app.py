import streamlit as st
from services.gemini_service import GeminiMarketAnalysisService

# Configurar la página
st.set_page_config(
    page_title="Nexus Alpha - Market Analysis",
    page_icon="📊",
    layout="wide"
)

# Título de la aplicación
st.title("📊 Nexus Alpha - Análisis de Mercado con Gemini")
st.markdown("---")

# Inicializar el servicio
@st.cache_resource
def get_service():
    return GeminiMarketAnalysisService()

service = get_service()

# Sidebar con opciones
st.sidebar.title("⚙️ Opciones")
option = st.sidebar.radio(
    "Selecciona una acción:",
    ["Analizar Mercado", "Generar Reporte", "Acerca de"]
)

# Sección: Analizar Mercado
if option == "Analizar Mercado":
    st.header("🔍 Análisis de Mercado")
    
    market_data = st.text_area(
        "Ingresa los datos del mercado a analizar:",
        placeholder="Ej: Stock XYZ subió 5%, volumen aumentó 20%...",
        height=150
    )
    
    if st.button("📈 Analizar", key="analyze"):
        if market_data.strip():
            with st.spinner("Analizando con Gemini..."):
                try:
                    analysis = service.analyze_market(market_data)
                    st.success("✅ Análisis completado")
                    st.write(analysis)
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
        else:
            st.warning("Por favor ingresa datos de mercado")

# Sección: Generar Reporte
elif option == "Generar Reporte":
    st.header("📋 Generar Reporte")
    
    analysis_input = st.text_area(
        "Ingresa el análisis para generar un reporte:",
        placeholder="Ej: Tendencia alcista con resistencia en...",
        height=150
    )
    
    if st.button("📄 Generar Reporte", key="report"):
        if analysis_input.strip():
            with st.spinner("Generando reporte con Gemini..."):
                try:
                    report = service.generate_report(analysis_input)
                    st.success("✅ Reporte generado")
                    st.write(report)
                    
                    # Botón para descargar
                    st.download_button(
                        label="📥 Descargar Reporte",
                        data=report,
                        file_name="reporte_mercado.txt",
                        mime="text/plain"
                    )
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
        else:
            st.warning("Por favor ingresa un análisis")

# Sección: Acerca de
elif option == "Acerca de":
    st.header("ℹ️ Acerca de Nexus Alpha")
    
    st.write("""
    ### 🎯 Descripción
    **Nexus Alpha** es una aplicación inteligente de análisis de mercado que utiliza 
    la API de **Google Gemini** para proporcionar análisis profundos y reportes detallados.
    
    ### ✨ Características
    - 📊 Análisis de datos de mercado en tiempo real
    - 🤖 Powered by Google Gemini AI
    - 📈 Generación automática de reportes
    - 💾 Descarga de reportes en formato texto
    
    ### 🔧 Tecnologías
    - **Streamlit**: Framework para la interfaz
    - **Google Gemini**: API de IA para análisis
    - **Python**: Lenguaje de programación
    
    ### 📞 Soporte
    Para más información, visita el repositorio en GitHub.
    """)
    
    st.info("✅ La aplicación está lista para usar")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "<p>Nexus Alpha v1.0 | Powered by Google Gemini</p>"
    "</div>",
    unsafe_allow_html=True
)
