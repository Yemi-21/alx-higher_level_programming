#!/usr/bin/python3
""" write_file module """
def append_write(filename="", text=""):
"""
        function that write a specific text in a specific file
        Args:
            fileName: name of the file
            text: text to write
    """   
    nbCharacter = 0
    with open(fileName, 'w', encoding="UTF-8") as file:
        nbCharacter = file.write(text)
    file.closed
    return nbCharacter
