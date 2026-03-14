def fact(n):
    if n==0 or n==1:
        
        return 1
    else:
        return n*fact(n-1)
def main():
    n=int(input("enter the number"))
    result=fact(n)
    print(f"the factorial of given number is{result}")
main()

 
