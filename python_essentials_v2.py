### The input Function is used to get data from the user, and the result is very useful.
#print("Hello User,I'm Jarvis")
#name = input("Please tell me your name.\n")
#anything = input(f"{name}, Please tell me anything you want to say to me\n")
#print(f"So {anything} is what you have to say,interesting...")

### Now we have to take a exercise that is interesting, a potentiation calculator

#number = int(input("Dame un numero para elevar\n"))
#exponente = int(input("Dame un exponente\n"))
#potenciado = number ** exponente
#print(f"{number} elevado a la {exponente} es {potenciado}")

### now what if we use string operators

#h1 = input("Dame por favor tu primer nombre\n")
#
#h2 = input("Dame tu apellido por favor\n")
#
#ced = (input("Dame tu cedula\n"))
#
#print(f"Señor {h1} {h2}, titular de la cedula de identidad:{ced}, usted ha sido hackeado")

###Now we are going to replicate a couple of strings and numbers

#print("Hello Python " * 3)
#print("Hello my friend " * 3 + "OMG " * 8 , end ="|")
#print ("Hi I'm a string")

###Now we are going to make a kind of weird calculator

#a = int(input("Please Give a number\n"))
#b = int(input("Please Give another number\n"))
#
#suma = a + b
#resta = a - b
#multiplicacion = a * b
#division = a / b
#
#print(f"{a} mas {b} es {suma}")
#print(f"{a} menos {b} es {resta}")
#print(f"{a} por {b} es {multiplicacion}")
#print(f"{a} dividido por {b} es {division}")

#I could do it more efficient but i love to do variables with no sense
#if you want to do it efficient just use this code

a = int(input("Please Give a number\n"))
b = int(input("Please Give another number\n"))

print(f"{a} mas {b} es", a + b)
print(f"{a} menos {b} es", a - b)
print(f"{a} multiplicado por {b} es", a * b)
print(f"{a} dividido por {b} es", a // b)