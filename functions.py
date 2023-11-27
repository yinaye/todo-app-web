FILE_NAME = "todos.txt"


def get_todos(filename=FILE_NAME):
    with open(FILE_NAME, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local):
    with open(FILE_NAME, "w") as file_local:
        file_local.writelines(todos_local)
