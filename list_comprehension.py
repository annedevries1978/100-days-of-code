#!python

# list comprehension
Celsius = [39.2, 25, 28.4, 16.6]
Fahrenheit = [((float(9)/5)*x + 32) for x in Celsius]

print(Fahrenheit)

# Generator comprehension
x = (x**2 for x in range(1,21))
print(x)
x=list(x)
print(x)

x = (x**3 for x in range(1,100) if x < 9)
# starts at number 26
print(list(x))