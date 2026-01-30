from entities.Todo import Todo
from repositories.TodoRepository import TodoRepository

class TodoService():
    def __init__(self, todo_repository: TodoRepository):
        self.todo_repository = todo_repository

    def show_todos(self):
        todos = self.todo_repository.get_all_todos()
        print("Daftar Todo:")
        if not todos:
            print("- Data todo belum tersedia!")
            return

        for counter, todo in enumerate(todos, start=1):
            print(todo)

    def add_todo(self, title: str):
        new_todo = Todo(title=title)
        self.todo_repository.add_todo(new_todo)

    def remove_todo(self, id: int):
        success = self.todo_repository.remove_todo(id)
        if not success:
            print(f"[!] Gagal menghapus todo dengan ID: {id}.")
