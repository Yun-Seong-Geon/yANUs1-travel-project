import streamlit as st
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def scroll(html, element_id):
    return html.replace('</body>'.encode(), """
    <script>
        var element = document.getElementById("{}");
        element.scrollIntoView();
    </script>
    </body>
    """.format(element_id).encode())
