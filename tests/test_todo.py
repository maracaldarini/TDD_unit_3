import pytest
from lib.todo import *

"""
Initialiser
when a new instance of Todo() is initialised
todo.todolist returns an empty list
"""
def test_initialiser():
    todo = Todo()
    assert todo.todolist == []

"""
Given a task
.add adds the task to the self list
"""
def test_add():
    todo = Todo()
    todo.add("Walk the dog")
    assert todo.todolist == ["Walk the dog"]

"""
Given a task that is not a string
.add raises an error
"""
def test_add_task_not_a_string():
    todo = Todo()
    with pytest.raises(Exception) as e:
        todo.add(2)
    error_message = str(e.value)
    assert error_message == "Please submit tasks as strings."

"""
After I have added one or more tasks
.see_tasks returns a list of tasks
"""
def test_see_tasks():
    todo = Todo()
    todo.add("Walk the dog")
    todo.add("Do homework")
    assert todo.see_tasks() == ["Walk the dog", "Do homework"]

"""
If I have not added any tasks
.see_tasks raises an error
"""
def test_see_tasks_empty_list():
    todo = Todo()
    with pytest.raises(Exception) as e:
        todo.see_tasks()
    error_message = str(e.value)
    assert error_message == "No tasks set."

"""
Given a task
.delete deletes the task from the self list, if the task is in the list
"""
def test_delete():
    todo = Todo()
    todo.add("Walk the dog")
    todo.add("Do homework")
    todo.delete("Walk the dog")
    assert todo.see_tasks() == ["Do homework"]

"""
If .delete is called with a task not present in the self list
An error is raised
"""
def test_delete_non_existing_task():
    todo = Todo()
    todo.add("Walk the dog")
    todo.add("Do homework")
    with pytest.raises(Exception) as e:
        todo.delete("Eat cake")
    error_message = str(e.value)
    assert error_message == "Task not found."