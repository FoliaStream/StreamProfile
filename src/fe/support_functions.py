import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd

import os 

from streamlit_option_menu import option_menu
from src.fe.styles import SIDEBAR_STYLES


# SIDEBAR
def setup_sidebar(pages,
                  main_page):
    with st.sidebar:
        col1, col2, col3 = st.columns([0.2, 2.4, 0.2])
        with col2:
            st.image(f"{os.getcwd()}/db/input/img/profile.jpg", use_container_width=True)

            

        
        # Initialize session state for page if it doesn't exist
        if 'selected_page' not in st.session_state:
            st.session_state.selected_page = main_page
        
        choose = option_menu("", 
                            pages,
                            default_index=pages.index(st.session_state.selected_page),
                            styles=SIDEBAR_STYLES)
        
        # Download PDF
        pdf_path = f"{os.getcwd()}/db/input/pdf/CV_SamueleBiasutti.pdf"
        
        if os.path.exists(pdf_path):
            with open(pdf_path, "rb") as pdf_file:
                PDFbyte = pdf_file.read()

            st.download_button(
                label="Download CV",
                data=PDFbyte,
                file_name="CV_SamueleBiasutti.pdf",
                mime="application/pdf",
                use_container_width=True
            )
        else:
            st.error("CV file not found.")
        
        # Refresh
        if choose != st.session_state.selected_page:
            st.session_state.selected_page = choose
            st.rerun()  
    
    return st.session_state.selected_page