def factorial(n):
    if n==0 or n==1:
        return 1
    else: return n*factorial(n-1)

n = int(input("Enter Number whose factorial you want"))

factorial = factorial(n)
print(factorial)
