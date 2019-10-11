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

    a = 0

    while a < len(text):
        if text[a] is "." or text[a] is "?" or text[a] is ":":
            print(text[a])
            print()
            a += 2
        else:
            print(text[a], end='')
            a += 1
