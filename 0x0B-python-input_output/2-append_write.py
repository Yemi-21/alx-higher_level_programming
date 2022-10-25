#!/usr/bin/python3
""" append_write module """


def append_write(filename="", text=""):
    """
        function that add specific text to a specific file

        Args:
            filename: name of the file
            text: text to add
    """
    nbCharacter = 0
    with open(filename, 'a', encoding="UTF-8") as file:
        nbCharacter = file.write(text)
    file.closed
    return nbCharacter
