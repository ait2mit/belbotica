import streamlit as st
from btools import BaseClass
import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")




text_df=pd.read_csv('text_source_for_web.csv')
bc = BaseClass()

im_path='images/bg.jpg'
processed_bg_img=bc.get_bg_to_display(im_path)
st.markdown(processed_bg_img, unsafe_allow_html=True)





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
    options2 = text_df['Main_Category'].values.tolist()[0:20] # Highest Defree
    skill_category = cols[0].selectbox("What is your hightest degree", options=options2)
    deg_text,im_path =bc.generate_text_for_hightest_degree(skill_category)

    cols[0].image(im_path, width=450, caption='Image Source: Unsplash')

    cols[1].subheader("Notes and Recommendations")


    cols[1].success(deg_text['description_texts1'])
    cols[1].markdown(deg_text['description_texts2'])
    cols[1].info(deg_text['description_texts3'])
    cols[1].success(deg_text['description_texts4'])
    cols[1].markdown(deg_text['description_texts5'])
    cols[1].info(deg_text['description_texts6'])
elif maingrp == options1[2]:
    options2 = text_df['Main_Category'].values.tolist()[20:27] # Technical Skilss
    skill_category = cols[0].selectbox("Let's Talk about your technical skills", options=options2)
    st.write(skill_category)

    if skill_category=='Data Science Toolbox':
        im_path='images/toolbox.jpg'
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
        your_data_st = cols[1].multiselect("Have you used these data structure before", options=['array','strings', 'integer','floats','lists' , 'tuples', 'sets', 'dict','collections', 'linkedlist'])
        your_loop = cols[1].multiselect("How often you use bash scripts ", options=['while loop','for Loop', 'if-else Loop'])
        your_doo = cols[1].text_input("Define Object Oriented programming")
        your_difoo = cols[1].selectbox("Can you differentiate between Procedural Programming vs. OOP", options=["Yes", 'No'])
        your_fun = cols[1].multiselect("Can you explain follwoing terms in your own words", options=['Function','Module','Package', 'Classes','Constructors','Objects', 'Instances'])
        your_pak = cols[1].multiselect("Which of these packages you are familer", options=['Numpy','Pandas','Matplotlib', 'sklearn','seaborn', 'dask'])
        your_pdf = cols[1].multiselect("Which of pandas function you have use before", options=['Columns rename','apply','groupby','to_datetime','reading and writing of csv files', 'others'])
        your_plot = cols[1].multiselect("What kind of plots you have created before", options=['Line plot','Boxplot','violine plot','catplot','histogram', 'others'])
        your_ds_plotpak = cols[1].multiselect("Which of the plotting packages have you use before", options=['matplotlib.pyplot','seaborn','plotly','bokeh','vega', 'others'])
        your_db = cols[1].multiselect("Have you used any of the following database for any purpose", options=['MySQL','Postgresql','Others'])
        your_dbf = cols[1].multiselect("Which of the basic labels background you have", options=['Create Database','Create Table','Make queries', 'Make Joins'])
        your_dbt = cols[1].multiselect("HAve you use any of the following or similar tools", options=['DBeaver','XAMP','Others'])


    elif skill_category=='Data Science Landscape':
        im_path='images/landscape.jpg'
        cols[0].image(im_path, width=450)
        cols[1].success("Let's summerize your Data Science skill sets")
        your_dsl1 = cols[1].selectbox("Do you know what is exploratory data analysis (EDA)", options=['Yes', 'No'])
        your_dsl2 = cols[1].selectbox("Do you know why we do EDA", options=['Yes', 'No'])
        your_dsl3 = cols[1].selectbox("Do you know what is Categorical variable", options=['Yes', 'No'])
        your_dsl4 = cols[1].selectbox("Do know how to counts nan value in a columns", options=['Yes', 'No'])
        your_dsl5 = cols[1].selectbox("Do you know know to treat nan value in your dataset", options=['Yes', 'No'])
        your_dsl6 = cols[1].selectbox("Do you know what is corelation coefficient and why they are imporntnat", options=['Yes', 'No'])
        your_dsl7 = cols[1].multiselect("Do you know what is feature and target ", options=['Yes', 'No'])

        your_dsl8 = cols[1].selectbox("Do you know what is the interquartile range or IQR", options=['Yes', 'No'])
        your_dsl9 = cols[1].selectbox("Do you know what is outliers", options=['Yes', 'No'])
        your_dsl10 = cols[1].selectbox("Do You know any method to identify outliers", options=['Yes', 'No'])


        your_dsl11 = cols[1].multiselect("Which of the following terms you can explain", options=['Supervised learning','Unsupervised learning','Semi-supervised learning', 'Instances'])
        your_dsl12 = cols[1].multiselect("Which of the following terms you can explain", options=['Classification','Regression','Clusering'])
        your_dsl13 = cols[1].multiselect("Which of pandas function you have use before", options=['Columns rename','apply','groupby','to_datetime','reading and writing of csv files', 'others'])
        your_dsl14 = cols[1].multiselect("What kind of plots you have created before", options=['Line plot','Boxplot','violine plot','catplot','histogram', 'others'])
        your_dsl15 = cols[1].multiselect("Which of the plotting packages have you use before", options=['matplotlib.pyplot','seaborn','plotly','bokeh','vega', 'others'])
        your_dsl16 = cols[1].multiselect("Have you used any of the following database for any purpose", options=['MySQL','Postgresql','Others'])
        your_dsl17= cols[1].multiselect("Which of the basic labels background you have", options=['Create Database','Create Table','Make queries', 'Make Joins'])
        your_dsl18 = cols[1].multiselect("HAve you use any of the following or similar tools", options=['DBeaver','XAMP','Others'])

    elif skill_category=='Machine Learning':
        im_path='images/ml.jpg'
        cols[0].image(im_path, width=450)
        cols[1].success("Let's summerize your ML skill sets")

        your_ml1 = cols[1].selectbox("Do you know what is Machine Learning (ML)", options=['Yes', 'No'])
        your_ml2 = cols[1].selectbox("Do you know what is model and modelling", options=['Yes', 'No'])
        your_ml3 = cols[1].selectbox("Do you know difference beteen ML model and Statistical Model", options=['Yes', 'No'])
        your_ml4 = cols[1].selectbox("Have you ever developed any ML model", options=['Yes', 'No'])
        your_ml5 = cols[1].selectbox("Do you know why we spit data before developing a ML model", options=['Yes', 'No'])
        your_ml6 = cols[1].selectbox("Do you know the difference between testset and validation dataset", options=['Yes', 'No'])
        your_ml7 = cols[1].selectbox("Do you know the difference between regression and classification", options=['Yes', 'No'])
        your_ml8 = cols[1].selectbox("Do you know the difference between balanced and imblanced", options=['Yes', 'No'])
        your_ml9 = cols[1].multiselect("Which of these algorithm you have used before ", options=['XGboost', 'Random Forest',' Decsion Tree','SVM', \
                                        'Logistic regression', 'Linear Regression', 'Naivebase', 'DL', 'RL'])

        your_ml10 = cols[1].multiselect("Which of these algorithm you can explain ", options=['XGboost', 'Random Forest',' Decsion Tree','SVM', \
                                        'Logistic regression', 'Linear Regression', 'Naivebase', 'DL', 'RL'])

        your_ml11 = cols[1].selectbox("Can you handle imbalance dataset", options=['Yes', 'No'])
        your_ml12 = cols[1].selectbox("What you will do if see an imbalance dataset", options=['smote', 'upsample','downsample','modify threshold'])
        your_ml13 = cols[1].selectbox("Do you know what is confusion matrix?", options=['Yes', 'No'])
        your_ml14 = cols[1].multiselect("Which of these you can explain without internet search?", options=['true positives (TP)', 'true negatives (TN)',\
                                            'false positives (FP)','false negatives (FN)'])
        your_ml15 = cols[1].multiselect("Which of these you can explain without internet search?", options=['True Positive Rate', 'False Positive Rate',\
                                            'True Negative Rate'])
        your_ml16 = cols[1].multiselect("Which of these you can explain without internet search?", options=['Accuracy', 'Precision',\
                                                        'Recall','Specificity'])

        your_ml17 = cols[1].selectbox("Do you know any python package name for model explainability", options=['Yes', 'No'])
        your_ml18 = cols[1].selectbox("Do you know why we need a model explainability package", options=['Yes', 'No'])
        your_ml19 = cols[1].multiselect("Which of these python package you have used?", options=['SHAP', 'Lime','ELI5',\
                                                        'Shapash','ExplainerDashboard','Dalex','Explainable Boosting Machines (EBM)'])


    elif skill_category=='DevOps':
        im_path='images/devops.jpg'
        cols[0].image(im_path, width=450)
        cols[1].success("Let's summerize your DevOps skill sets")

        your_do1 = cols[1].selectbox("Do you know what is DevOps?", options=['Yes', 'No'])
        your_do1 = cols[1].selectbox("Do you know what is CI/CD Pipeline", options=['Yes', 'No'])
        your_do1 = cols[1].selectbox("Have you used deployed anything using CI/CD Pipeline", options=['Yes', 'No'])
        your_do1 = cols[1].selectbox("Have you ever used YAML file?", options=['Yes', 'No'])
        your_do1 = cols[1].selectbox("Do you know what is docker?", options=['Yes', 'No'])
        your_do1 = cols[1].selectbox("Have you seen any Dockerfile", options=['Yes', 'No'])
        your_do1 = cols[1].selectbox("Do you know what is kubernettes", options=['Yes', 'No'])
        your_do1 = cols[1].selectbox("In which situation we may use Dockerand Kuberneteis", options=['Yes', 'No'])
        your_do1 = cols[1].selectbox("Do you know anything about docker compose or docker swarm?", options=['Yes', 'No'])
        your_do1 = cols[1].selectbox("Have you used MLFlow?", options=['Yes', 'No'])
        your_do1 = cols[1].selectbox("Do you know what is Jenkins", options=['Yes', 'No'])
        your_do1 = cols[1].selectbox("Have you ever used Jenkins?", options=['Yes', 'No'])

    elif skill_category=='Big Data':
        im_path='images/bigdata.jpg'
        cols[0].image(im_path, width=450)
        cols[1].success("Let's summerize your DevOps skill sets")

        your_bg1 = cols[1].selectbox("Do you know what is Big Data?", options=['Yes', 'No'])
        your_bg2 = cols[1].selectbox("Do you know what 4Vs of Big Data?", options=['Yes', 'No'])
        your_bg3 = cols[1].selectbox("Can you define how large data is Big Data", options=['Yes', 'No'])
        your_bg4 = cols[1].multiselect("Which of these big data terms you can explain", options=['4Vs', '5Vs','Hadoop','MapReduce','Spark','Storm'])
        your_bg5 = cols[1].selectbox("Do you know difference between Hadoop and Big Data", options=['Yes', 'No'])
        your_bg6 = cols[1].multiselect("Have your use any of these technology", options=['Hadoop', 'Spark','PySpark', 'SparkR','Scala'])
        your_bg7 = cols[1].selectbox("Have you done EDA using any Big Data Technology (e.g., PySpark)", options=['Yes', 'No'])
        your_bg8 = cols[1].multiselect("Which of these Big Data technology you can explain", options=['Hive', 'MLLib','Pig'])
        your_bg9 = cols[1].selectbox("Can you develop a machine learning model using PySpark or Spark R?", options=['No', 'Yes','Working on it'])

    elif skill_category=='Cloud Technology':
        im_path='images/cloud.jpg'
        cols[0].image(im_path, width=450)
        cols[1].success("Let's summerize your DevOps skill sets")

        your_ct1 = cols[1].multiselect("Please select which cloud servcies you have used before?", options=['AWS', 'Azure','GCP','SnowFlakes', 'Others'])
        your_ct2 = cols[1].multiselect("Have you used any of the following products from AWS?", options=['EC2', 'S3','SageMaker','Lambda','Glue','EMR','ECS','ECR','Api Gateway', 'RedShift','DynamoDB', 'Others'])
        your_ct = cols[1].multiselect("Have you used any of the following products from Azure?", options=['Yes', 'No'])


        your_ct3 = cols[1].multiselect("Which of these big data terms you can explain", options=['4Vs', '5Vs','Hadoop','MapReduce','Spark','Storm'])
        your_ct4 = cols[1].selectbox("Do you know difference between Hadoop and Big Data", options=['Yes', 'No'])
        your_ct5 = cols[1].multiselect("Have your use any of these technology", options=['Hadoop', 'Spark','PySpark', 'SparkR','Scala'])
        your_ct6 = cols[1].selectbox("Have you done EDA using any Big Data Technology (e.g., PySpark)", options=['Yes', 'No'])
        your_ct7 = cols[1].multiselect("Which of these Big Data technology you can explain", options=['Hive', 'MLLib','Pig'])
        your_ct8 = cols[1].selectbox("Can you develop a machine learning model using PySpark or Spark R?", options=['No', 'Yes','Working on it'])






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
