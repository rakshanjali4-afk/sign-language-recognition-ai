def linear_search(arr,key):
    for i in  range (len(arr)):
        if arr[i]==key:
            return i
    return-1
def binary_search(arr,key):
    low,high=0,len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1    
    return-1
arr=[]
item=int(input("enter the size"))
for j in range(item):
    values=int(input("the items are"))
    arr.append(values)
key=int(input("enter the key value"))
print("linear search",linear_search(arr,key))
print("binary search",binary_search(arr,key))
