#!/usr/bin/python3
""" read_file module """


def read_file(filename=""):
 """
        function that read specific file

        Args:
            filename: name of the file
    """
  with open(filename, encoding="UTF-8") as file:
        read_data = file.read()
        print(read_data, end="")
    file.closed
