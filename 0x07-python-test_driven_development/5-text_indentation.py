#!/usr/bin/python3
def text_indentation(text):

    """
    Indentation of a text separated by special characters
    """

    if type(text) is not str or text is None or len(text) < 0:
        """Conditional for value is string"""
        raise TypeError("text must be a string")
    else:
        pass


    new_txt = str(text)
    new_line = False
    for a in new_txt:
        if new_line:
            if a is " ":
                continue
            new_line = False
        if a is "." or a is "?" or a is ":":
            print(a)
            print("")
            new_line = True
        else:
            print(a, end='')
