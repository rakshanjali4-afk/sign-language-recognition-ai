import os
file_name = input("Enter the file name (with .txt): ")

try:
    with open(file_name, "r") as file:
        text = file.read()

    words = text.lower().split()
    unique_words = sorted(set(words))

    print("Unique words:", unique_words)

except FileNotFoundError:
    print("File not found! Make sure the file is in the same folder.")