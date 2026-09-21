import streamlit as st 
import os 
import yaml 

from src.fe.support_functions import setup_sidebar
from src.fe.styles import HIDE_SIDEBAR_NAV, CARD_STYLES

################
# --- SET UP ---
################

st.set_page_config(page_title="CAREER", layout="wide")

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
    pass
elif selected_page == "PROJECTS":
    st.switch_page("pages/PROJECTS.py")

# --- MAIN CONTENT ---
with st.container():
    st.markdown("<h1 style='color: #005B9F; margin-bottom: 2rem;'> Career History</h1>", unsafe_allow_html=True)

    # --- 1. CORPORATE & TECHNICAL EXPERIENCE ---
    st.markdown("<h3 style='color: #005B9F; margin-bottom: 1rem;'> Corporate & Technical Experience</h3>", unsafe_allow_html=True)
    html_corporate = """
    <div class="custom-card">
        <div class="date">Business Development Engineer, Decarbonization Modelling | Wärtsilä Italy (Feb 2024 - Feb 2026)</div>
        <p>Contributed to the development of simulation models that evaluate the feasibility and economic impact of decarbonization retrofit projects, utilizing Python to collect, analyze, and process large datasets for assessing the viability of decarbonization technologies. Delivered technical and economic reports to customers and stakeholders, while implementing structural improvements in workflows and tools to enhance operational efficiency.</p>
        <div class="date">Project Purchaser | Wärtsilä Italy (Jul 2023 - Feb 2024)</div>
        <p>Supported Parts Supply department through market analysis, feasibility studies, and qualification of new propulsion solutions. The major operational tasks involved the use of SAP for the identification and procurement of spare parts from suppliers to storages and/or end users, and the analysis of historical orders data to optimize parts supply process.</p>
        <div class="date">Junior Financial Consulting Manager | Diacron Business Consulting Co. Ltd., Shanghai (Dec 2022 - Jun 2023)</div>
        <p>A 6-months learning experience based in Asia. While collaborating with an international team of senior managers and consultants, I contributed to several financial and accounting tasks, compiling Excel documents, reviewing financial reports, and interacting with clients and a team Chinese accountants. In addition, I applied my technical programming capabilities to implement an Excel VBA based interface aiming to optimize the overall workflow dedicated to compiling financial reports.</p>
    </div>
    """
    st.markdown(html_corporate.replace('\n', ''), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True) # Space between sections

    # --- 2. TEACHING & VOLUNTEERING EXPERIENCE ---
    st.markdown("<h3 style='color: #005B9F; margin-bottom: 1rem;'> Teaching & Volunteer Experience</h3>", unsafe_allow_html=True)
    html_teaching = """
    <div class="custom-card">
        <div class="date">English Teacher | PoPoDoo Center Thanh Mien, Vietnam (Apr 2026 - Present)</div>
        <p>Teaching English at PoPoDoo English Center in Thanh Mien town, Hai Phong. I have instructed hundreds of students ranging from 4 to 25 years old. While my work with younger learners focuses on building foundational vocabulary, I also prepare advanced students for Cambridge and IELTS examinations through targeted practice and test-preparation strategies.</p>
        <div class="date">Teacher English Speaking & Listening Extra Course | Vietnam (Feb 2026 - Present)</div>
        <p>Currently tutoring 2 classes of Vietnamese students aged between 7 and 14 years old through an English course focused on the development of speaking, writing, listening, and reading skills.</p>
        <div class="date">Project Contributor - Teacher Ethical Debate | Vietnam (Nov 2025 - Jan 2026)</div>
        <p>Helped coordinate a debate initiative involving multiple Vietnamese students. The program was designed to strengthen participants' debating, speaking, listening, and critical thinking abilities, all while engaging with meaningful ethical topics.</p>
        <div class="date">Volunteer | Viet-Skype (2025)</div>
        <p>Served as a volunteer English teacher for this non-profit organization in Vietnam, delivering free lessons to students across various age groups and proficiency levels. Through one-on-one tutoring, I helped learners improve their speaking accuracy, fluency, grammar, and vocabulary.</p>
        <div class="date">Assistant | China-Italy Chamber of Commerce, Shanghai (Sep 2022 - Dec 2022)</div>
        <p>Contributed to the organization of social events, webinar, and networking activities for more than 750 Italian companies located in China. Besides my primary tasks, I implemented, organized, and structured an Excel database and dedicated search engine.</p>
    </div>
    """
    st.markdown(html_teaching.replace('\n', ''), unsafe_allow_html=True)