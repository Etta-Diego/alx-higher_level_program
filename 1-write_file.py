#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf8") as f:
            f.write(text)
            return len(text)
