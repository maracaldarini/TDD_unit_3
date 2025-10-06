from lib.count_words import *

def test_return_number_words_in_string():
    result = count_words("brave new world")
    assert result == 3
