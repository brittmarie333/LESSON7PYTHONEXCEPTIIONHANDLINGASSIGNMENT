#Task 2: Temperature Conversion Write a function that converts the Fahrenheit temperature to Celsius. 
# Remember that the formula is (Fahrenheit - 32) * 5/9.

try:
    current_temperature = float(input("Provide your temperature in Fahrenheit: "))
    print("It is ", current_temperature, " degrees Farenheit outside!")
except ValueError:
    print("Invalid input. Please enter a number.")