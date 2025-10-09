class Todo():
    def __init__(self):
        self.todolist = []

    def add(self, task):
        if type(task) is str:
            self.todolist.append(task)
        else:
            raise Exception("Please submit tasks as strings.")

    def see_tasks(self):
        if len(self.todolist) > 0: 
            return self.todolist
        else:
            raise Exception("No tasks set.")

    def delete(self, task):
        if self.todolist.count(task) > 0:
            self.todolist.remove(task)
        else:
            print(self.todolist.count(task))
            raise Exception("Task not found.")



