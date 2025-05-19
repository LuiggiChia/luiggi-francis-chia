import streamlit as st
import time
from streamlit_carousel import carousel

st.set_page_config(page_title="Luiggi Portfolio", page_icon="💯")

if "language" not in st.session_state:
    st.session_state.language = "en"

def toggle_language():
    st.session_state.language = "es" if st.session_state.language == "en" else "en"

lang = st.session_state.language
button_label = "Cambiar a español" if lang == "en" else "Switch to English"
col1, col2, col3 = st.columns(3)
with col3:
    st.button(button_label, on_click=toggle_language)

TEXTS = {
    "en": {
        "greeting": "Hi, my name is Luiggi",
        "intro": "I'm a data specialist from Lima, Peru. I'm focused on advancing my career in tech and to further my expertise in this world of data.",
        "about_title": "About me",
        "about_body": "I am currently a Pricing Analyst at <span style='color:#64ffda;'>Tottus</span>, working in the area of pricing analytics. At the same time, I am taking courses to further specialize.",
        "tech_title": "Here are some technologies I have been working with:",
        "exp_title": "Experience",
        "exp1_company": "Tottus",
        "exp1_bullets": [
            "Creating predictive models.",
            "Creating queries in GCP for data flow automation.",
        ],
        "exp2_company": "Arellano",
        "exp2_bullets": [
            "Extraction, cleaning and processing of data for subsequent analysis.",
            "Generation and maintenance of reports and dashboards.",
        ],
        "cert_title": "Certificates",
    },
    "es": {
        "greeting": "Hola, mi nombre es Luiggi",
        "intro": "Soy especialista de datos de Lima, Perú. Estoy enfocado en impulsar mi carrera en tecnología y profundizar mi experiencia en este mundo de datos.",
        "about_title": "Sobre mí",
        "about_body": "Actualmente soy Analista de Precios en <span style='color:#64ffda;'>Tottus</span>, trabajando en el área de analítica de precios. Al mismo tiempo, llevo cursos para especializarme aún más.",
        "tech_title": "Algunas tecnologías con las que he trabajado:",
        "exp_title": "Experiencia",
        "exp1_company": "Tottus",
        "exp1_bullets": [
            "Creación de modelos predictivos.",
            "Construcción de consultas en GCP para automatizar flujos de datos.",
        ],
        "exp2_company": "Arellano",
        "exp2_bullets": [
            "Extracción, limpieza y procesamiento de datos para análisis posterior.",
            "Generación y mantenimiento de reportes y dashboards.",
        ],
        "cert_title": "Certificados",
    },
}

t = TEXTS[lang]

text_placeholder = st.empty()
for i in range(len(t["greeting"]) + 1):
    text_placeholder.markdown(f"<h1>{t['greeting'][:i]}</h1>", unsafe_allow_html=True)
    time.sleep(0.05)

st.markdown(
    f"<p style='text-align: center;'>{t['intro']}</p>",
    unsafe_allow_html=True,
)

st.markdown(f"<h3 style='color:#ccd6f6'>{t['about_title']}</h3>", unsafe_allow_html=True)
st.markdown(f"<p>{t['about_body']}</p>", unsafe_allow_html=True)

st.markdown(f"<p>{t['tech_title']}</p>", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .two-columns {display:flex; gap:50px;}
    .two-columns ul {list-style-type: disc; padding-left:20px;}
    .two-columns li::marker {color:#64ffda; font-size:18px;}
    </style>

    <div class="two-columns">
        <ul><li>Python</li><li>SQL</li></ul>
        <ul><li>Power BI</li><li>Microsoft Excel</li></ul>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(f"<h3 style='color:#ccd6f6'>{t['exp_title']}</h3>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"<p style='text-align:center; color:#64ffda'>{t['exp1_company']}</p>", unsafe_allow_html=True)
    st.markdown(
        """
        <style>
        .two-columns {display:flex; gap:50px;}
        .two-columns ul {list-style-type: disc; padding-left:20px;}
        .two-columns li::marker {color:#64ffda; font-size:18px;}
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        "<ul>" + "".join(f"<li>{item}</li>" for item in t["exp1_bullets"]) + "</ul>",
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(f"<p style='text-align:center; color:#64ffda'>{t['exp2_company']}</p>", unsafe_allow_html=True)
    st.markdown(
        """
        <style>
        .two-columns {display:flex; gap:50px;}
        .two-columns ul {list-style-type: disc; padding-left:20px;}
        .two-columns li::marker {color:#64ffda; font-size:18px;}
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        "<ul>" + "".join(f"<li>{item}</li>" for item in t["exp2_bullets"]) + "</ul>",
        unsafe_allow_html=True,
    )

st.markdown(f"<h3 style='color:#ccd6f6'>{t['cert_title']}</h3>", unsafe_allow_html=True)
items = [
    {"title": "", "text": "", "img": f"images/Certificado{i}.jpg"}
    for i in range(1, 10)
]
carousel(items=items)

# st.link_button("LinkedIn", "https://www.linkedin.com/in/tu-perfil")
