#passing arguments

def add(a,b):
    return a + b


def multiply(a,b):
    return a * b

operation = input("Enter the operation: ")
a = int(input("enter first value: "))
b = int(input("enter the second number: "))
if operation == "+":
    ans = add(a,b)
    print(ans)

elif operation == "*":
    ans = multiply(a,b)
    print(ans)
else:
    print("invalid operator: ")