import streamlit as st
import streamlit.components.v1 as components
from front_login import login_html
import utils as fd
import streamlit_authenticator as stauth
import front_register as fs
def login_page():
    fd.local_css("streamlitCss/login.css")
    # st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    components.html(login_html,width=1200,height=700)
    
login_page()