#!/usr/bin/python3
""" read_file module """
def read_file(FileName=""):
    """
        function that read specific file
        Args:
            FileName: name of the file
    """
    with open(FileName, encoding="UTF-8") as file:
        read_data = file.read()
        print(read_data, end="")
    file.closed
