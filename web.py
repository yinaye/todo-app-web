import streamlit as st
import functions

st.title("My Todo List")
st.subheader("This is a todo list")
st.write("The tool is to improve productivity")

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)


for index, todo in enumerate(todos):
    print(f"{index}-{todo}")
    checkbox_key = f"{index}-{todo}"
    checkbox = st.checkbox(todo, key=checkbox_key)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[checkbox_key]
        st.rerun()

st.text_input(label=" ", label_visibility="hidden",
              on_change=add_todo,
              placeholder="Enter a todo...", key="new_todo")
