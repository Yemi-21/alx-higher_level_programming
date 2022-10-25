#!/usr/bin/python3

def append_write(filename="", text=""):
   
    nbCharacter = 0
    with open(fileName, 'w', encoding="UTF-8") as file:
        nbCharacter = file.write(text)
    file.closed
    return nbCharacter
