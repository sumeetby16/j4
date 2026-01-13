a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

add = a + b
print(f"Addition: {a} + {b} = {add}")

sub = a - b
print(f"Subtraction: {a} - {b} = {sub}")

mul = a * b
print(f"Multiplication: {a} * {b} = {mul}")

if b != 0:
    div = a / b
    print(f"Division: {a} / {b} = {div}")
else:
    print("Division: Cannot divide by zero")

