import pandas as pd
import streamlit as st

movies = [

    {"course_name": "Data Analyst", "keywords": ["powerbi", "tableau","data analysis", "python","pandas","numpy"]},
    {"course_name": "Digital Marketing", "keywords": ["affiliatemarketing", "emailmarketing"]},
    {"course_name": "Python", "keywords": ["data science", "programming language","machine  learning","oops","python","numpy"]},
    {"course_name": "Java Full Stack Developer", "keywords":["oops", "javascript", "html", "css"]},
    {"course_name": "Cyber Security Solutions", "keywords": ["firewall", "data security"]},
    {"course_name": "Game Designer", "keywords": ["2d and 3d animation", "prototyping", "UI and UX"]},
    {"course_name": "Graphic Designer", "keywords": ["typography", "colortheory", "animation"]},
    {"course_name": "Back End Developer", "keywords": ["database", "mongoDB", "css", "javascript"]},
    {"course_name": "Front End Developer", "keywords": ["javascript", "react", "front end frameworks"]},
    {"course_name": "Network Engineer", "keywords": ["network configuration and optimization", "firewall", "network security"]},
    {"course_name": "Mobile App Development", "keywords": ["app analytics", "ar and vr", "javascript"]},
    {"course_name": "Cloud Computing Services", "keywords": ["ms azure", "google cloud platform", "python"]},
    {"course_name": "Excel Analytics", "keywords": ["data analysis", "lookup functions", "conditional formatting"]},
    {"course_name": "Business Analytics", "keywords": ["data visualization", "business intelligence", "sql", "tableau"]},
    {"course_name": "Data visualisation using Tableau", "keywords": ["tableau", "dashboards", "data visualisation"]},
    {"course_name": "IT Automation Solutions", "keywords": ["powershell", "kubernetes", "java", "sql"]},
    {"course_name": "Software Development", "keywords": ["bootstrap", "cloud9", "web development", "java"]},
    {"course_name": "Mobile App Development", "keywords": ["adobe phonegap", "unity", "javascript"]},
    {"course_name": "Web Design Development", "keywords": ["UI&UX", "css", "javascript"]},
    {"course_name": "Java Automation Testing", "keywords": ["oops", "file operations", "database"]},
    {"course_name": "Big Data", "keywords": ["data warehousing", "data analysis", "sql"]},
    {"course_name": "Cloud Analytics", "keywords": ["aws", "ms azure", "python", "sql"]},
    {"course_name": "Animation in Motion Graphics", "keywords": ["storytelling", "brand messaging", "UI and UX"]},
    {"course_name": "Artificial Intelligence", "keywords": ["machine learning", "deep learning", "python"]},
    {"course_name": "Google Data Analytics", "keywords": ["data storytelling with visualizations","data analysis", "sql", "tableau"]},
    {"course_name": "Predictive Modeling", "keywords": ["data mining", "machine learning", "r"]},
    {"course_name": "R programming", "keywords": ["data analysis", "statistical computing", "data visualization"]},
    {"course_name": "SQL", "keywords": ["data integrity", "data security", "mysql"]},
    {"course_name": "Advanced Excel for Data Analysis", "keywords": ["conditional formatting", "lookup functions", "ms excel"]},
    {"course_name": "SAP", "keywords": ["analysis and forecasting", "cost effectiveness", "database"]},
    {"course_name": "C++", "keywords": ["compilers", "cloud storage systems", "oops"]},
    {"course_name": "Advanced Java", "keywords": ["error handling and exception handling", "type conversion", "oops"]},
    {"course_name": "Adobe Photoshop", "keywords": ["web design", "digital design", "graphics"]},
    {"course_name": "Ethical Hacking", "keywords": ["security hacking", "network security"]},
    {"course_name": "Zoho CRM", "keywords": ["workflow automation", "contextual communication", "customization"]},
    {"course_name": "Data Analytics using Pandas", "keywords": ["data selection", "data frame", "data analysis"]},
    {"course_name": "MongoDB", "keywords": ["rich query capabilities", "python", "java"]},
    {"course_name": "Oracle", "keywords": ["payroll", "workforce management", "sql"]},
    {"course_name": "Programming Fundamentals", "keywords": ["oops", "data structure"]},
    {"course_name": "Quantum Computing and Its Applications", "keywords": ["material science", "climate modeling"]},
    {"course_name": "Xmind", "keywords": ["problem solving", "decision making", "mapping tool"]},
    {"course_name": "Staad Pro", "keywords": ["3d modeling", "structural analysis"]},
    {"course_name": "Rust Programming", "keywords": ["command line tools", "building kernels"]},
    {"course_name": "React JS", "keywords": ["debugging", "rendering", "front end frameworks"]},
    {"course_name": "Natural Language Processing With Python", "keywords": ["stemming", "deep learning","lemmatization"]},
    {"course_name": "Tableau", "keywords": ["data visualisation", "tableau", "data analysis"]}
]

with st.sidebar:
    input_title = st.text_input("Search..")

    input_genres = []
    for movie in movies:
        if movie['course_name'].lower() == input_title.lower():
            input_genres = movie['keywords']

    st.subheader("RECOMMENDATIONS FOR YOU")
    recommended_movies = []
    for movie in movies:
        if movie['course_name'].lower() != input_title.lower():
            if any(genre in input_genres for genre in movie['keywords']):
                recommended_movies.append(movie['course_name'])
    for j in recommended_movies:
        st.text(j)

# For display
st.title("RECOMMENDATION SYSTEM")
st.header("COURSES")

cols = st.columns(3)
for idx, movie in enumerate(movies):
    with cols[idx % 3]:
        st.text(movie['course_name'])
