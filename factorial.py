def factorial(x):
    if x <= 1:
        return 1
    else: 
        return x * factorial(x - 1) 
fact = factorial(5)
print(fact)
print("Yes")
print("No")