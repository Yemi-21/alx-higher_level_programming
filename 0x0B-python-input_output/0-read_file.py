#!/usr/bin/python3
def read_file(fileName=""):
   with open(fileName, encoding="UTF-8") as file:
        read_data = file.read()
        print(read_data, end="")
    file.closed
