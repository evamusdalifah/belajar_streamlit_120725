import streamlit as st
st.set_page_config(page_title="Portfolio",
                   layout="wide", page_icon=":rocket:")
st.title("Portfolio Saya")
st.header("Data Scientist")
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman",
                        ["About", "Project_1", "Project_2"])


if page == 'About' :
    import about
    about.about()
elif page == 'Project_1' : 
    import project_1
    project_1.projectsatu()
elif page == 'Project_2' : 
    import project_2
    project_2.projectdua()
