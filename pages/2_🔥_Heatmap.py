import streamlit as st
from btools import BaseClass
bc = BaseClass()
st.set_page_config(layout="wide")

markdown = """
Web App URL: <https://template.streamlitapp.com>
GitHub Repository: <https://github.com/giswqs/streamlit-multipage-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)


im_path='images/bg.jpg'
processed_bg_img=bc.get_bg_to_display(im_path)
st.markdown(processed_bg_img, unsafe_allow_html=True)












st.title("Heatmap")
