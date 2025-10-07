import pytest
from lib.calculate_reading_time import *

def test_calculate_reading_time_200_words_or_more():
    string = "In today’s fast-paced world, the ability to adapt and learn quickly is more important than ever. Technology is advancing at an unprecedented rate, reshaping the way we live, work, and communicate. As a result, individuals and organizations alike must prioritize continuous learning to stay relevant and competitive. Lifelong learning isn’t just a buzzword—it’s a necessity. Whether you’re learning a new language, mastering a piece of software, or understanding a new market trend, consistent effort leads to meaningful growth. This approach fosters resilience and creativity, equipping people with the tools to navigate change effectively. It also helps build confidence, as knowledge gained over time empowers better decision-making. Educational opportunities today are more accessible than ever before. Online courses, podcasts, webinars, and digital communities provide countless ways to gain new skills. With so many options available, learning can be personalized to fit any schedule or interest. Ultimately, the pursuit of knowledge should be viewed not as a task, but as a privilege. Embracing curiosity leads to innovation and greater fulfillment. By fostering a mindset of continuous improvement, both individuals and societies can thrive, no matter what challenges the future brings. The journey never ends—and that’s a good thing four more words here."
    result = calculate_reading_time(string)
    assert result == "1 minute(s)"

def test_calculate_reading_time_less_than_200_words():
    string = "In today’s fast-paced world"
    result = calculate_reading_time(string)
    assert result == "Less than 1 minute"

def test_calculate_reading_time_empty_string():
    string = ""
    with pytest.raises(Exception) as e:
        result = calculate_reading_time(string)
    error_message = str(e.value)
    assert error_message == "There is no text!"

def test_calculate_reading_time_not_a_string():
    string = 70
    with pytest.raises(Exception) as e:
        result = calculate_reading_time(string)
    error_message = str(e.value)
    assert error_message == "There is no text!"
