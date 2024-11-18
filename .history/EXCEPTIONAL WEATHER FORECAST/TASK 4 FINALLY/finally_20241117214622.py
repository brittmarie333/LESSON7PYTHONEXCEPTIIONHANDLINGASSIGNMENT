#Task 4: Finally Add a finally block that thanks the user for using the weather forecast application, 
# ensuring that this message is displayed regardless of whether an exception was caught or not.

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    print("Temperature in Celsius:", round(celsius, 3), "degrees.")


try:
    fahrenheit = float(input("Provide your temperature in Fahrenheit: "))
    fahrenheit_to_celsius(fahrenheit)
except ValueError:
    print("Invalid input. Please enter a number.")
else:
    print("The tempearture is: ", fahrenheit, "degrees Farenheit")
finally:
    print("Thank you for ")