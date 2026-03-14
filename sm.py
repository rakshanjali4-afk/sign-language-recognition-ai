file_name=input("enter the filename")
with open(file_name,"r") as file:
    text=file.read()
words=text.lower().split()
un=sorted(set(words))
print(un)    