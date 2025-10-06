from lib.make_snippet import *

# A function called make_snippet that takes a string as an argument and returns the first five words and then a '...' if there are more than that.

def test_return_string():
    result = make_snippet("")
    assert result == ""

def test_return_full_string_if_under_six_words():
    result = make_snippet("one two three four five")
    assert result == "one two three four five"

def test_return_first_five_words():
    result = make_snippet("The doors of perception and heaven and hell")
    assert result == "The doors of perception and..."
