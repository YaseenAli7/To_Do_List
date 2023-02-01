import json
from PyQt5 import QtCore, QtGui, QtWidgets

file = "tasks.json"

def load_tasks():
    try:
        with open(file, "r") as f:
            return json.load(f)
    except:
        return []

def save_tasks(tasks):
    with open(file, "w") as f:
        json.dump(tasks, f)

class ToDoList(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List")
        self.setGeometry(200,200,500,500)
        self.create_widgets()
        self.refresh_list()

    def create_widgets(self):
        self.task_entry = QtWidgets.QLineEdit(self)
        self.task_entry.move(50,50)

        self.date_entry = QtWidgets.QLineEdit(self)
        self.date_entry.move(50,100)

        self.add_button = QtWidgets.QPushButton("Add",self)
        self.add_button.move(50,150)
        self.add_button.clicked.connect(self.add_task)

        self.task_list = QtWidgets.QListWidget(self)
        self.task_list.setGeometry(QtCore.QRect(50, 200, 400, 250))

        self.delete_button = QtWidgets.QPushButton("Delete", self)
        self.delete_button.move(50,475)
        self.delete_button.clicked.connect(self.delete_task)

    def add_task(self):
        task = self.task_entry.text()
        date = self.date_entry.text()
        tasks = load_tasks()
        tasks.append({'task': task, 'date': date})
        save_tasks(tasks)
        self.refresh_list()

    def refresh_list(self):
        self.task_list.clear()
        tasks = load_tasks()
        for task in tasks:
            self.task_list.addItem(f"{task['task']} - {task['date']}")

    def delete_task(self):
        tasks = load_tasks()
        selected = self.task_list.currentRow()
        if selected == -1:
            QtWidgets.QMessageBox.warning(self, "Error", "No task selected")
        else:
            del tasks[selected]
            save_tasks(tasks)
            self.refresh_list()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    todo = ToDoList()
    todo.show()
    app.exec_()