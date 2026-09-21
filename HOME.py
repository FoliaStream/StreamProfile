import streamlit as st 
import os 
import yaml 

from src.fe.support_functions import setup_sidebar
# Import both style variables
from src.fe.styles import HIDE_SIDEBAR_NAV, CARD_STYLES

################
# --- SET UP ---
################

# --- PAGE CONFIG --- 
st.set_page_config(page_title="HOME", layout="wide")

# --- STYLES ---
st.markdown(HIDE_SIDEBAR_NAV, unsafe_allow_html=True)
st.markdown(CARD_STYLES, unsafe_allow_html=True) # <-- Apply your card styles here

# --- CONFIG ---
with open(f"{os.getcwd()}/src/be/config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)

# --- SIDEBAR & TITLE ---
selected_page = setup_sidebar(
    pages=config['pages'],
    main_page=config['main_page'])

# Navigation on click
if selected_page == "HOME":
    pass
elif selected_page == "EDUCATION":
    st.switch_page("pages/EDUCATION.py")
elif selected_page == "CAREER":
    st.switch_page("pages/CAREER.py")
elif selected_page == "PROJECTS":
    st.switch_page("pages/PROJECTS.py")

# --- MAIN CONTENT ---
with st.container():
    # --- GENERAL INFORMATION SECTION ---
    st.markdown("""
    <div class="info-card">
        <h1>Samuele Biasutti</h1>
        <div class="details">
            <strong>Contact:</strong> &nbsp;|&nbsp; <a href="mailto:biasuttil8@gmail.com">biasuttil8@gmail.com</a> &nbsp;|&nbsp; 17-06-1997 &nbsp;|&nbsp; <a href="https://www.linkedin.com/in/samuele-biasutti-165290193/" target="_blank">LinkedIn Profile </a> &nbsp;|&nbsp;
            <br><br>
            Data and technical solutions professional with an engineering and economics background, combining data-driven modelling, techno-economic analysis and application development. Master's in Technology and Operations Management from the University of Groningen. Two years of experience in Wärtsilä's Decarbonization Modelling team, turning large operational datasets into simulation models and investment cases for customers and stakeholders. End-to-end development of data-driven applications, from databases and Python APIs to cloud-deployed web frontends, several of them released as open-source tools. Experience with international teams and clients across Europe and Asia, translating technical concepts into business value through client-facing reporting, teaching and coaching. Based in Vietnam.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- RECAP CONTAINERS (Horizontal Layout) ---
    col_edu, col_career, col_proj = st.columns(3)

    # 1. EDUCATION Container
    with col_edu:
        st.markdown("<h3 style='color: #005B9F; margin-bottom: 1rem;'> Education</h3>", unsafe_allow_html=True)
        st.markdown("""
        <div class="custom-card-home">
            <div class="extra">MSc Technology & Operations </div>
            <div class="date">University of Groningen (2021 - 2022) </div>
            <p>Specialized in Data Analysis, Operations Modelling, and Sustainability. Thesis focused on optimizing carbon capture infrastructure across Europe.</p>
            <div class="extra">BSc Economics & Business Economics</div>
            <div class="date">University of Groningen (2017 - 2022)</div>
            <p>Focused on Statistics, Finance, and International Economics with a strong foundation in data-driven economic research.</p>

        </div>
        """, unsafe_allow_html=True)

    # 2. CAREER Container
    with col_career:
        st.markdown("<h3 style='color: #005B9F; margin-bottom: 1rem;'> Career</h3>", unsafe_allow_html=True)
        st.markdown("""
        <div class="custom-card-home">
            <div class="extra">Business Development Engineer</div>
            <div class="date">Wartsila Italy (2024 - 2026)</div>
            <p>Developed simulation models for decarbonization retrofit projects using Python. Delivered technical and economic feasibility reports.</p>
            <div class="extra">English Teacher</div>
            <div class="date">PoPoDoo Center, Vietnam (2026 - Present)</div>
            <p>Teaching English to students aged 4-25, preparing advanced learners for Cambridge and IELTS examinations.</p>

        </div>
        """, unsafe_allow_html=True)

    # 3. PROJECTS Container
    with col_proj:
        st.markdown("<h3 style='color: #005B9F; margin-bottom: 1rem;'> Projects</h3>", unsafe_allow_html=True)
        st.markdown("""
        <div class="custom-card-home">
            <div class="extra"> Developer</div>
            <div class="date">FoliaStream ~ FoliaNova ~ TEFL Architect ~ FSRU CCC</div>
            <p>Designed and developed multiple open-source Streamlit web apps. These tools address complex problems ranging from optimal network structures for carbon capture to forest offset calculations and educational support tools.</p>

        </div>
        """, unsafe_allow_html=True)