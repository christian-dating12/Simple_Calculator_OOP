# Christian M. Dating | BSCPE 1-5 | MINI CALCULATOR - OOP

# Create a Simple App Calculator | OOP
# 1. The application will ask the user to choose one of the four math operations (Addition, Subtraction, Multiplication, Division)
# 2. The application will ask the user for two numbers.
# 3. Display the result.
# 4. The application will ask the user wants to try again or not.
# 5. If yes, repeat step 1
# 6. If no, Display "Thank you!" and the program will exit.
# 7. Use Python Function and appropriate Exeptions to capture errors during runtime.

# PSEUDOCODE

from user_interface import user_interface

ui = user_interface()


# Ask the user for two inputs
# input 1
num1 = ui.ask_input1()
# input 2
num2 = ui.ask_input2()

# Ask the user to choose one of the four math operations (Addition, Subtraction, Multiplication, Division)
# Math operations choices
print("ADDITION")
print("SUBTRACTION")
print("MULTIPLICATION")
print("DIVISION")
# Display the result
# Ask the user to try again or not
# If yes, repeat step 1
# If no, display "Thank you"