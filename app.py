import streamlit as st
import pandas as pd
import datetime
import random
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
                dueDate = st.date_input("Due Date") 
                dueTime = st.time_input("Due Time", value = datetime.time(23,59))
                points = st.number_input("Points")
                assignmentWeight = st.number_input("What percent of your grade would this assignment affect?")  

                if (assignmentName!=""):
                    randomKey = random.randint(100000, 999999)
                    create_tasks(assignmentName, dueDate, dueTime, assignmentWeight, points, randomKey)

                submit_button = st.form_submit_button()

                if submit_button:
                    
                    st.success("Task Created")
                    with col2:
                        st.empty()
                        st.subheader("Tasks")
                        tasks = get_tasks()
                        for task in tasks:
                            st.write("Assignment Name: " + str(task["assignmentName"]))
                            st.write("Due Date: " + str(task["dueDate"]))
                            st.write("Due Time: " + str(task["dueTime"]))
                            st.write("Assignment Weight: " + str(task["assignmentWeight"]))
                            st.write("priority value: " + str(task["priorityValue"]))
                            st.write("id: " + str(task["id"]) )

                            st.button("Completed", key=task["id"])
                                
                
                            st.markdown('#')
    





                
    # if choice == "Classes":
    #     st.subheader("Classes")
    #     with st.form(key = "createClass"):
    #         className = st.text_input("Class Name")
    #         create_classes(className)
    #         submit_button = st.form_submit_button()
    #     if submit_button:
    #         st.success("Class Created")
    
        


            

    

if __name__ == '__main__':
    main()