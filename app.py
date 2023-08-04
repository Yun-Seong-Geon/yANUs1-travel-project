import streamlit as st
import streamlit.components.v1 as components
import front_login as fl
import utils as fd
import streamlit_authenticator as sa
from streamlit_javascript import st_javascript
import front_register as fs
from pages.로그인 import login_page
st.set_page_config(layout='wide',page_title='GAN',initial_sidebar_state='auto')
st.set_option('deprecation.showPyplotGlobalUse', False)



def main():
    
    login_page()
    ##st.write(fl.login_id)
    
if __name__ == "__main__":
    main()