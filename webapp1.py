##this version creates the web-based to do list application

import functions
import streamlit as st

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("Stuff I need to do")
st.write("The <b>Official</b> Get-it-done list",
         unsafe_allow_html=True)

for index, todo in enumerate(todos):
    checkbox=st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)