import streamlit as st
import pandas as pd

st.set_page_config(page_title="My Todo List", page_icon=":smiley:")

def main():
    st.title("Streamlit Todo List")
    menu = ["Create","View","Classes"]
    choice = st.sidebar.selectbox("Menu",menu)
    classes = [];
    if choice == "Create":
        st.subheader("Home")
        with st.form(key = "createTask"):
            assignmentName = st.text_input("Assignment Name")
            assignmentClass = st.selectbox("Assignment Class", classes)
            dueDate = st.date_input("Due Date")
            dueTime = st.time_input("Due Time")
            submit_button = st.form_submit_button()
        if submit_button:
            st.success("Task Created")
    if choice == "Classes":
        st.subheader("Classes")
        with st.form(key = "createClass"):
            className = st.text_input("Class Name")
            submit_button = st.form_submit_button()
        if submit_button:
            st.success("Class Created")
    
        

    

    

if __name__ == '__main__':
    main()