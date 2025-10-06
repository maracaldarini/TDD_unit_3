def make_snippet(string):
    words_list = string.split()
    first_five = " ".join(words_list[:5])
    if len(words_list) < 6:
        return first_five
    else:
        
        return first_five + "..."