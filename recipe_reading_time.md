# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def calculate_reading_time(text):
    """Calculates reading time based on number of words

    Parameters: (list all parameters and their types)
        string: a string that represents a text

    Returns: (state the return value and its type)
        an int, the total number of minutes required to read the given text

    Side effects: (state any side effects)
       This function also calculates the number of words in the given string as an int
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a string with a wordcount over 200
It returns an estimate of reading time as a string
"""
calculate_reading_time(str) => "1 minute"

"""
Given a string with a wordcount under 200
It returns an estimate of reading time as a string
"""
calculate_reading_time(str) => "Less than 1 minute"

"""
Given an empty string
It returns 0
"""
calculate_reading_time("") => 0

"""
Given a None value
It throws an error
"""
calculate_reading_time(None) throws an error

"""
Given a parameter that is not a string
It throws an error
"""
calculate_reading_time(70) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
