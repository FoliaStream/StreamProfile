import streamlit as st 
import os 
import yaml 

from src.fe.support_functions import setup_sidebar
# Importing CARD_STYLES based on your updated styles.py
from src.fe.styles import HIDE_SIDEBAR_NAV, CARD_STYLES

################
# --- SET UP ---
################

# --- PAGE CONFIG --- 
st.set_page_config(page_title="EDUCATION", layout="wide")

# --- STYLES ---
st.markdown(HIDE_SIDEBAR_NAV, unsafe_allow_html=True)
st.markdown(CARD_STYLES, unsafe_allow_html=True)

# --- CONFIG ---
with open(f"{os.getcwd()}/src/be/config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)

# --- SIDEBAR & TITLE ---
selected_page = setup_sidebar(
    pages=config['pages'],
    main_page=config['main_page'])

# Navigation on click
if selected_page == "HOME":
    st.switch_page("HOME.py")
elif selected_page == "EDUCATION":
    pass
elif selected_page == "CAREER":
    st.switch_page("pages/CAREER.py")
elif selected_page == "PROJECTS":
    st.switch_page("pages/PROJECTS.py")


# --- MAIN CONTENT ---
with st.container():
    # Header
    st.markdown("<h1 style='color: #005B9F; margin-bottom: 2rem;'> Education & Qualifications</h1>", unsafe_allow_html=True)

    # --- 1. ACADEMIC DEGREES ---
    st.markdown("<h3 style='color: #005B9F; margin-bottom: 1rem;'> Academic Degrees</h3>", unsafe_allow_html=True)
    html_degrees = """
    <div class="custom-card">
        <div class="date">MSc Technology and Operations Management | University of Groningen, Netherlands (Sep 2021 - Aug 2022)</div>
        <p>Mainly focused on Data Analysis and Programming, Operations Management and Control, Operations Modelling and Simulation. Besides the main focus on optimizing supply chain dynamics using a data analytical approach, I followed courses concerning sustainability, energy transition and innovation. My thesis project involved the implementation and optimization of a carbon capture utilization and storage infrastructure in 6 different European countries, adopting different renewable energy sources.</p>
        
        <div class="date">BSc Economics & Business Economics | University of Groningen, Netherlands (Sep 2017 - Aug 2022)</div>
        <p>Mainly focused on Statistics, Finance, Business, and International Economics. I chose the Economics profile specialization: high-practical and theoretical foundation in Data Analysis, Micro and Macro-economics, Economic Growth, and Strategic Behaviour. A crucial part of the curriculum was devoted to investigating economic research questions using the statistical approach.</p>
        
        <div class="date">Highschool Scientific Lyceum Guglielmo Oberdan | Trieste, Italy (2010 - 2016)</div>
        <p>Applied sciences profile - focused on informatics, advanced mathematics, and scientific subjects.</p>
    </div>
    """
    st.markdown(html_degrees.replace('\n', ''), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True) # Add some space between the sections

    # --- 2. LANGUAGES & CERTIFICATIONS ---
    st.markdown("<h3 style='color: #005B9F; margin-bottom: 1rem;'> Languages & Certifications</h3>", unsafe_allow_html=True)
    html_certs = """
    <div class="custom-card">
        <div class="date">Languages</div>
        <p><strong>Italian:</strong> Native proficiency<br>
        <strong>English:</strong> Full professional proficiency<br>
        <strong>Mandarin:</strong> Intermediate proficiency</p>

        <div class="date">Mandarin Certifications</div>
        <p><strong>HSK 4 and Business Chinese</strong> - Le Nuove Vie della Seta Trieste, Italy (2025)<br>
        <strong>HSK 1, 2, 3</strong> - Groningen Confucius Institute, Netherlands (2022)</p>

        <div class="date">English Certifications</div>
        <p><strong>Proficiency certificates:</strong> TOEFL exam - score: 100+; IELTS exam - score: 8 (2025)<br>
        <strong>Teaching certificates:</strong> TEFL; TESOL; Teach English to Young Learners - International TEFL Academy (2025)</p>
    </div>
    """
    st.markdown(html_certs.replace('\n', ''), unsafe_allow_html=True)