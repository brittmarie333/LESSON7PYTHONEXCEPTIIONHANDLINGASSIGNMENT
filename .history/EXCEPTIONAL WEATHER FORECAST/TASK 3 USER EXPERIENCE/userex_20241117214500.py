#Task 3: User Experience Implement an else block that prints the converted temperature in a user-friendly format. 

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    print("Temperature in Celsius:", round(celsius, 3))


try:
    fahrenheit = float(input("Provide your temperature in Fahrenheit: "))
    fahrenheit_to_celsius(fahrenheit)
except ValueError:
    print("Invalid input. Please enter a number.")
else:
    print("The tempearture is: ", fahrenheit, )