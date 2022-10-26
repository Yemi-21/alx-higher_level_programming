#!/usr/bin/python3
""" write_file module """


def write_file(filename="", text=""):
    """
        function that write a specific text in a specific file

        Args:
            filename: name of the file
            text: text to write
    """
    nbCharacter = 0
    with open(filename, 'w', encoding="UTF-8") as file:
        nbCharacter = file.write(text)
    file.closed
    return nbCharacter
