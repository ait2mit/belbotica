import streamlit as st
from btools import BaseClass
import pandas as pd
st.set_page_config(layout="wide")

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)



text_df=pd.read_csv('text_source_for_web.csv')
bc = BaseClass()



# Customize the sidebar
markdown = """
Web App URL: <https://bengalai.com>

"""
# Customize page title
st.title("General Suggestions to the pathway of Data Scientist")


options1 = [" Select an Option", "Educational", "Technical Skills", "Other Skills"]
maingrp = st.sidebar.selectbox("Select Your evaluation Matrix", options=options1)
cols = st.columns((1, 2))
if maingrp == options1[1]:
    options2 = text_df['Main_Category'].values.tolist()[0:21] # Highest Defree
    skill_category = cols[0].selectbox("What is your hightest degree", options=options2)
    deg_text,im_path =bc.generate_text_for_hightest_degree(skill_category)

    cols[0].image(im_path, width=450)
    cols[1].subheader("Notes and Recommendations")


    cols[1].success(deg_text['description_texts1'])
    cols[1].markdown(deg_text['description_texts2'])
    cols[1].info(deg_text['description_texts3'])
    cols[1].success(deg_text['description_texts4'])
    cols[1].markdown(deg_text['description_texts5'])
    cols[1].info(deg_text['description_texts6'])
elif maingrp == options1[2]:
    options2 = text_df['Main_Category'].values.tolist()[20:24] # Technical Skilss
    skill_category = cols[0].selectbox("Let's Talk about your technical skills", options=options2)
    st.write(skill_category)

    if skill_category=='Data Science Toolbox':
        im_path='images/toolbx.jpg'
        cols[0].image(im_path, width=450)
        cols[1].success("Let's summerize your Data Science Toolbox skill sets")
        your_os = cols[1].multiselect("What is your main OS", options=['macOS','Linux','Windows', 'WSL'])
        your_bash = cols[1].selectbox("How often you use bash scripts ", options=['Rarely','Sometimes','When needed', 'I hate bash scripts'])
        your_ide = cols[1].selectbox("What is your main IDE / Editor", options=['VS Code','Atom','Sublime', 'Emacs'])
        your_ds_pro = cols[1].multiselect("What is your main Programming Language", options=['Python','R','Others'])
        your_python = cols[1].selectbox("What is your Pyhon Version", options=['3.10','3.9','3.8', '3.7','3.6','2.7'])
        your_r = cols[1].text_input("What is your R and R Studio Versions:")
        your_git = cols[1].multiselect("What is your version control platfom", options=['No Experience','GitLab','Github','Bitbucket','Others'])
        your_bidata = cols[1].multiselect("Which big data technologies you have used before", options=['No Experience','Hadoop','PySpark','SparkR','Others'])
        your_bidata = cols[1].multiselect("Which big data technologies you have used before", options=['No Experience','Jupyter','Anaconda','Google Colab','Others'])

    elif skill_category=='Programming':
        im_path='images/prog.jpg'
        cols[0].image(im_path, width=450)
        cols[1].success("Let's summerize your Data Science Toolbox skill sets")
        your_os = cols[1].multiselect("Have you used these data structure before", options=['array','strings', 'integer','floats','lists' , 'tuples', 'sets', 'dict','collections', 'linkedlist'])
        your_bash = cols[1].multiselect("How often you use bash scripts ", options=['while loop','for Loop', 'if-else Loop'])
        your_r = cols[1].text_input("Define Object Oriented programming")
        your_python = cols[1].selectbox("Can you differentiate between Procedural Programming vs. OOP", options=["Yes", 'No'])
        your_ide = cols[1].multiselect("Can you explain follwoing terms in your own words", options=['Function','Module','Package', 'Classes','Constructors','Objects', 'Instances'])
        your_ide = cols[1].multiselect("Can you explain follwoing terms in your own words", options=['Function','Module','Package', 'Classes','Objects', 'Instances'])
        your_ds_pro = cols[1].multiselect("What is your main Programming Language", options=['Python','R','Others'])


        your_git = cols[1].multiselect("What is your version control platfom", options=['No Experience','GitLab','Github','Bitbucket','Others'])
        your_bidata = cols[1].multiselect("Which big data technologies you have used before", options=['No Experience','Hadoop','PySpark','SparkR','Others'])







elif maingrp == options1[3]: # Other Skills
    options2 = text_df['Main_Category'].values.tolist()[25:30]
    skill_category = cols[0].selectbox("How about other skills", options=options2)
    cols[1].title("Please see our comments")

    # deg_text =bc.generate_text_for_hightest_degree(skill_category)
    # cols[1].success(deg_text['description_texts1'])
    # cols[1].markdown(deg_text['description_texts2'])
    # cols[1].info(deg_text['description_texts3'])
    # cols[1].success(deg_text['description_texts4'])
    # cols[1].markdown(deg_text['description_texts5'])
    # cols[1].info(deg_text['description_texts6'])








st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)
