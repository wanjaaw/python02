#A statement that assigns a value to a variable.
#To join two operands end to end.

age = 29
name = "Agnes"
age = str(29)
print('My name is '+ name + 'my age is '+ age)

age = 29
name = "Agnes"
age = str(29)
print('My name is '+ name + ' ' + 'my age is '+ age)
# python programming glossary 
# Exercise 2
# Write a program that uses input to prompt a user for their name and then welcomes them.
name = 'Chuck'
print('Hello ' + name)

# Exercise 3
# Write a program to prompt the user for hours and rate per hour to compute gross pay.

hours = int(input('no of hours'))
rate = 2.75
rate = float(2.75)
pay = hours * rate
print(pay)

# Exercise 4
#Assume that we execute the following assignment statements
width = 17
height = float(12.0)
m = width // 2
n = width / 2.0
p = height / 3
q = 1 + 2 * 5
print( m , n, p, q)
print(type(m), type(n), type(p), type(q))


# Exercise 5: Write a program which prompts the user 
#for a Celsius temperature, convert the temperature to Fahrenheit, 
#and print out the converted temperature.
# Formula	
#(1°C × 9/5) + 32 = 33.8°F
temp_c = float(input('celsius temprature'))
temp_f = float(input('farenheit temprature'))
converter_f = temp_c * (9/5) + 32
converter_c = (temp_f - 32) * (5/9)
print(converter_c, 'celsius')
print(converter_f, 'farenheit')

#imports on math and random
# Exercise 1
# Run the program on your system and see what numbers you get. 
# Run the program more than once and see what numbers you get.
