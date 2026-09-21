import streamlit as st 
import os 
import yaml 

from src.fe.support_functions import setup_sidebar
from src.fe.styles import HIDE_SIDEBAR_NAV, CARD_STYLES

################
# --- SET UP ---
################

st.set_page_config(page_title="PROJECTS", layout="wide")

st.markdown(HIDE_SIDEBAR_NAV, unsafe_allow_html=True)
st.markdown(CARD_STYLES, unsafe_allow_html=True)

with open(f"{os.getcwd()}/src/be/config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)

selected_page = setup_sidebar(
    pages=config['pages'],
    main_page=config['main_page'])

if selected_page == "HOME":
    st.switch_page("HOME.py")
elif selected_page == "EDUCATION":
    st.switch_page("pages/EDUCATION.py")
elif selected_page == "CAREER":
    st.switch_page("pages/CAREER.py")
elif selected_page == "PROJECTS":
    pass

# --- MAIN CONTENT ---
with st.container():
    st.markdown("<h1 style='color: #005B9F; margin-bottom: 2rem;'> Projects & Applications</h1>", unsafe_allow_html=True)

    # --- 1. DATA & ENGINEERING APPLICATIONS ---
    st.markdown("<h3 style='color: #005B9F; margin-bottom: 1rem;'> Data & Engineering Applications</h3>", unsafe_allow_html=True)
    html_apps = """
    <div class="custom-card">

        <div class="date">Cryogenic Carbon Capture & FSRU Vessels</div>
        <p>Developed an open-source web app for evaluating the investment case for retrofitting Cryogenic Carbon Capture (CCC) technology onto Floating Storage and Regasification Units (FSRUs), grounded in peer-reviewed thermodynamic research. The app models vessel-specific TCO, NPV, IRR and payback period across EU ETS, FuelEU Maritime, and draft IMO carbon-pricing frameworks, comparing as-is versus retrofit scenarios. <br><a href="https://fsruccc.streamlit.app/" target="_blank">FSRU CCC LINK</a></p>

        <div class="date">FoliaStream</div>
        <p>Generated an open-source web app dedicated to the identification of optimal network structures for handling goods within a set of nodes. The first practical implementation has been generating optimal carbon capture and storage network structures at country level. <br><a href="https://foliastream.streamlit.app/" target="_blank">FoliaStream LINK</a></p>
        
        <div class="date">FoliaNova</div>
        <p>Designed a publicly available web app that uses worldwide industrial pollution data and forest information to show how much new forest would be needed to offset emissions from any given area or facility. <br><a href="https://folianova.streamlit.app/" target="_blank">FoliaNova LINK</a></p>
 
        <div class="date">TEFL Architect</div>
        <p>Designed an open-source web app focused on supporting teachers in their tasks. The tool itself aims to (1) simplify the courses and lessons preparation procedures, (2) provide an online repository where to share teaching material and documentation, and (3) support teachers with interactive tools to be used in-class. <br><a href="https://teflarchitect.streamlit.app/" target="_blank">TEFL Architect LINK</a></p>
    </div>
    """
    st.markdown(html_apps.replace('\n', ''), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True) # Space between sections

    # --- 2. BUSINESS & PROFESSIONAL PROJECTS ---
    st.markdown("<h3 style='color: #005B9F; margin-bottom: 1rem;'> Business & Professional Projects</h3>", unsafe_allow_html=True)
    html_business = """
    <div class="custom-card">
        <div class="date">Excel VBA Financial Interface | Diacron Business Consulting (2023)</div>
        <p>Applied technical programming capabilities to implement an Excel VBA based interface aiming to optimize the overall workflow dedicated to compiling financial reports. This tool significantly reduced manual data entry time and improved accuracy for the consulting team.</p>

        <div class="date">Chamber Database & Search Engine | China-Italy Chamber of Commerce (2022)</div>
        <p>Implemented, organized, and structured an Excel database and dedicated search engine to help manage and connect over 750 Italian companies located in China for social events, webinars, and networking activities.</p>
        
        <div class="date">Teacher Ethical Debate Coordinator | Vietnam (Nov 2025 - Jan 2026)</div>
        <p>Helped coordinate a debate initiative involving multiple Vietnamese students. The program was designed to strengthen participants' debating, speaking, listening, and critical thinking abilities, all while engaging with meaningful ethical topics.</p>
    </div>
    """
    st.markdown(html_business.replace('\n', ''), unsafe_allow_html=True)