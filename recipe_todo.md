# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class Todo:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:
        #   self.todolist: list()
        # Side effects:
        #   Sets the name property of the self object
        pass # No code here yet

    def add(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to self.todolist
        pass # No code here yet

    def see_tasks(self):
        # Returns:
        #   A list of the tasks still outstanding
        # Side-effects:
        #   Throws an exception if no task is set
        pass # No code here yet

    def completed(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects:
        #   Deletes the task from self.todolist
        #   Raises an error if the task is not in the list
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

"""
Given a task
.add adds the task to the self list
"""
todo = Todo()
todo.add("Walk the dog")
todo.todolist() # => ["Walk the dog"]

"""
After I have added one or more tasks
.see_tasks returns a list of tasks
"""
todo = Todo()
todo.add("Walk the dog")
todo.add("Do homework")
todo.see_tasks() # => ["Walk the dog", "Do homework"]

"""
If I have not added any tasks
.see_tasks raises an error
"""
rtodo = Todo()
todo.see_tasks() # raises an error with the message "No task set."

"""
Given a task
.delete deletes the task from the self list, if the task is in the list
"""
todo = Todo()
todo.add("Walk the dog")
todo.add("Do homework")
todo.delete("Walk the dog")
todo.see_tasks() # => ["Do homework"]

"""
If .delete is called with a task not present in the self list
An error is raised
"""
todo = Todo()
todo.add("Walk the dog")
todo.add("Do homework")
todo.delete("Eat cake")
todo.see_tasks() # => raises an error with the message "Task not found"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
