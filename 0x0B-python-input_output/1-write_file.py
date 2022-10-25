#!/usr/bin/python3





def write_file(filename="", text=""):

    with open(filename, "w", encoding="UTF-8") as f:

        return f.write(text)
"""#!/usr/bin/python3
""" write_file module """
def append_write(filename="", text=""):
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
    return nbCharacter"""
