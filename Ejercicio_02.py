#Ejercicio 2

# a = 20    --> a = 30
# b = 30    --> b = 20

a=input("a: ")
b=input("b: ")

a,b=b,a

print(f"El nuevo valor de a es: {a}")
print(f"El nuevo valor de b es: {b}")