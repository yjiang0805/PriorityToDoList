import streamlit as st
import pandas as pd

from db_function import *

st.set_page_config(page_title="My Todo List", page_icon=":smiley:")

def main():
    st.title("Priority To-Do List")
    menu = ["Create","Classes","View","Completed"]
    choice = st.sidebar.selectbox("Menu",menu)
    if choice == "Create":
        st.subheader("Home")
        with st.form(key = "createTask"):
            assignmentName = st.text_input("Assignment Name")
            classes = [i['className'] for i in get_classes()]
            assignmentClass = st.selectbox("Assignment Class", classes)
            dueDate = st.date_input("Due Date")
            dueTime = st.time_input("Due Time")
            assignmentWeight = st.number_input("What percent of your grade would this assignment affect?")
            task_status = st.selectbox("Status",["ToDo","Doing","Done"])
            submit_button = st.form_submit_button()
        if submit_button:
            create_tasks(assignmentName, assignmentClass, dueDate, dueTime, assignmentWeight,task_status)
            st.success("Task Created")
                        
    if choice == "Classes":
        st.subheader("Classes")
        with st.form(key = "createClass"):
            className = st.text_input("Class Name")
            submit_button = st.form_submit_button()
        if submit_button:
            create_classes(className)
            st.success("Class Created")
    if choice == "View":
        df = pd.DataFrame(get_tasks())
        st.dataframe(df)
    if choice == "Completed":
        tasks = [i['assignmentName'] for i in get_tasks()]
        option = st.selectbox("Items to Complete", tasks)
        if st.button("Complete"):
            delete_task(option)
            st.warning("Completed: '{}'".format(option))
            st.balloons()

if __name__ == '__main__':
    main()