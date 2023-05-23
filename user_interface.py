class user_interface:

    def ask_input1(self):
        num1 = float(input("Enter first number: "))
        return num1
    
    def ask_input2(self):
        num2 = float(input("Enter second number: "))
        return num2
    
    def input_op(self): 
        op =  str(input("Chosen operation: "))
        return op
    
    def display_sum(self, sum,):
        print ("Sum = ", + sum)

    def display_diff(self, diff):
        print ("Difference = ", + diff)

    def display_prod(self, prod):
        print ("Product = ", + prod)

    def display_quot(self, quot):
        print ("Quotient = ", + quot)

    def try_again(self):
        again = str(input("Do you want to try again (YES or NO) ? "))
        return again



    