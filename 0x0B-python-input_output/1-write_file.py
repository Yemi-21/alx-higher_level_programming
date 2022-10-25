#!/usr/bin/python3
""" write_file module """
def append_write(filename="", text=""):
    """
        function that write a specific text in a specific file
        Args:
            FileName: name of the file
            Text: text to write
    """
    nbCharacter = 0
    with open(FileName, 'w', encoding="UTF-8") as file:
        nbCharacter = file.write(Text)
    file.closed
    return 
