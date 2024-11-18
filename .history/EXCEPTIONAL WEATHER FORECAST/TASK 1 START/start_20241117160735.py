#Objective: The aim of this assignment is to enhance your understanding of exception handling by creating a weather forecast application 
# that gracefully handles unexpected user input and provides user-friendly error messages.

#Task 1: Start Begin by asking the user to enter the temperature in Fahrenheit.

def current_temperature():

    print(input("What is the temperature in farenheit?"))


while True:
    try:
        temp = float(input("Provide temperature in farenheit: "))
    return temp
except ValueError:
        print("Invalid input. Please enter a number")