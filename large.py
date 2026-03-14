num=[]
n=int(input("enter the size"))
for i in range (n):
    item=int(input("enter the element in the list"))
    num.append(item)
l=num[0]
for i in num:
    
    if i>l:
      l=i
print("largest item",l)            