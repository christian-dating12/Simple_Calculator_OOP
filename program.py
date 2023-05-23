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
from calculator import Calculator

ui = user_interface()
calcu = Calculator()

while True:
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


    op = ui.input_op()

# Display the result
 
    try:
        if op == ("ADDITION"):
            sum = calcu.add(num1, num2)
            ui.display_sum(sum)

        elif op == ("SUBTRACTION"):
            diff = calcu.subtract(num1, num2)
            ui.display_diff(diff)
    
        elif op == ("MULTIPLICATION"):
            prod = calcu.multiply(num1, num2)
            ui.display_prod(prod)

        elif op == ("DIVISION"):
            quot = calcu.divide(num1, num2)
            ui.display_quot(quot)

        else:
            print("\nInvalid. Please choose from the given operations above.")

# Ask the user to try again or not
        while True:
            again = ui.try_again()

# If yes, repeat step 1

            while True:
                if again == "YES":
                    break
                
# If no, display "Thank you"
                else:
                    print("THANK YOU!")
                    break

            if again == "YES":
                break
                
            elif again == "NO":
                    exit()  
                        
    except ValueError:
        while True:
            print("Invalid input. Please try again.")
            break
