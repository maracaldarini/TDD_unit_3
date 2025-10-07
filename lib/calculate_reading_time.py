def calculate_reading_time(text):
    if isinstance(text, str):
        wordcount = len(text.split(" "))
        if text == "":
            raise Exception("There is no text!")
        elif wordcount >= 200:
            minutes = int(wordcount / 200)
            return f"{minutes} minute(s)"
        elif wordcount < 200 and wordcount > 0:
            return "Less than 1 minute"
    else:
        raise Exception("There is no text!")