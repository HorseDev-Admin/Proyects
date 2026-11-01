### I need to introduce to you a simple calculator
name_of_user = input("Please give me your name User.\n")
print(f"Welcome {name_of_user} to my new calculator")
a = int(input("Please give me the first number\n"))
b = int(input("Please give me the second number\n"))
operador = int(input("Please give me the operation you want to do\n 1. is +\n 2. is -\n 3. is *\n 4. is /.\n"))
if operador == 1:
    print("Your Result is", a + b)
elif operador == 2:
    print("Your result is", a - b)
elif operador == 3:
    print("Your result is", a * b)
elif operador == 4:
    print ("Your result is", a / b)
else:
    print(f"{name_of_user} You introduced a invalid digit or string")