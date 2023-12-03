import streamlit as st
import pandas as pd
import datetime
import random
from db_function import *

st.set_page_config(page_title="My Todo List", page_icon=":smiley:")

def on_button_click(button):
    st.session_state.last_clicked = button

def clear_form():

    st.session_state["name"] = ""


def write_data():
    tasks = get_tasks()
    for task in tasks:
        st.write("Assignment Name: " + str(task["assignmentName"]))
        st.write("Due Date: " + str(task["dueDate"]))
        st.write("Due Time: " + str(task["dueTime"]))
        st.write("Assignment Weight: " + str(task["assignmentWeight"]))
        st.write("priority value: " + str(task["priorityValue"]))
        st.write("id: " + str(task["id"]) )
        st.button("Completed",key=task["id"], on_click=on_button_click, kwargs={"button": task["id"]})

def main():
    print("refresh")
    

    st.title("Priority To-Do List")
    menu = ["Create","Classes"]

    choice = st.sidebar.selectbox("Menu",menu)
    if choice == "Create":

        col1, col2 = st.columns(2)
        with col1:
            
            st.subheader("Home")
            with st.form(key = "createTask", clear_on_submit=True):
                
                assignmentName = st.text_input("Assignment Name")   
                print(assignmentName)
                dueDate = st.date_input("Due Date") 
                dueTime = st.time_input("Due Time", value = datetime.time(23,59))
                points = st.number_input("Points")
                assignmentWeight = st.number_input("What percent of your grade would this assignment affect?")  

                
                
                submit_button = st.form_submit_button()

                if submit_button:   
                    if not assignmentName.strip():
                        pass
                    else: 
                        randomKey = random.randint(100000, 999999)
                        create_tasks(assignmentName, dueDate, dueTime, assignmentWeight, points, randomKey)

                        st.success("Task Created")

                    with col2:
                        st.subheader("Tasks")
                        if 'last_clicked' not in st.session_state:
                            write_data()
                        


        if 'last_clicked' in st.session_state:
            remove_task(st.session_state["last_clicked"]) 
            with col2:
                col2 = st.empty()
                write_data()
            st.session_state["last_clicked"]=""
        st.write(st.session_state)
        


if __name__ == '__main__':
    main()