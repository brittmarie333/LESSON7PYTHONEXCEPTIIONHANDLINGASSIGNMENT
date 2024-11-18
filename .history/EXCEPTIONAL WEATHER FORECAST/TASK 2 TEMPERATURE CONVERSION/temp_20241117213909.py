#Task 2: Temperature Conversion Write a function that converts the Fahrenheit temperature to Celsius. 
# Remember that the formula is (Fahrenheit - 32) * 5/9.

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    print("Temperature in Celsius:", round(celsius, 3))


try:
    current_temperature = float(input("Provide your temperature in Fahrenheit: "))
    fahrenheit_to_celsius
except ValueError:
    print("Invalid input. Please enter a number.")