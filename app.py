import streamlit as st
import pandas as pd

from db_function import *

st.set_page_config(page_title="My Todo List", page_icon=":smiley:")

def main():
    st.title("Priority To-Do List")
    menu = ["Create","Classes"]
    choice = st.sidebar.selectbox("Menu",menu)
    if choice == "Create":
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Home")
            with st.form(key = "createTask"):
                assignmentName = st.text_input("Assignment Name")
                classes = [i['className'] for i in get_classes()]
                assignmentClass = st.selectbox("Assignment Class", classes[1:])
                dueDate = st.date_input("Due Date")
                dueTime = st.time_input("Due Time")
                assignmentWeight = st.number_input("What percent of your grade would this assignment affect?")
                create_tasks(assignmentName, assignmentClass, dueDate, dueTime, assignmentWeight)
                submit_button = st.form_submit_button()
                # st.balloons()
            if submit_button:
                st.success("Task Created")
                with col2:
                    st.subheader("Tasks")
                    tasks = get_tasks()
                    for task in tasks:
                        st.write("Assignment Name: " + str(task["assignmentName"]))
                        st.write("Assignment Class: " + str(task["assignmentClass"]))
                        st.write("Due Date: " + str(task["dueDate"]))
                        st.write("Due Time: " + str(task["dueTime"]))
                        st.write("Assignment Weight: " + str(task["assignmentWeight"]))
                        st.button("Completed")   
                        st.markdown('#')
                        
    if choice == "Classes":
        st.subheader("Classes")
        with st.form(key = "createClass"):
            className = st.text_input("Class Name")
            create_classes(className)
            submit_button = st.form_submit_button()
        if submit_button:
            st.success("Class Created")
    
        

    

    

if __name__ == '__main__':
    main()