class user_interface:

    def ask_input1(self):
        num1 = float(input("\nEnter first number: "))
        return num1
    
    def ask_input2(self):
        num2 = float(input("\nEnter second number: "))
        return num2
    
    def input_op(self): 
        op =  str(input("\nChosen operation: "))
        return op
    
    def display_sum(self, sum,):
        print ("\n\033[93mSum = ", + sum)

    def display_diff(self, diff):
        print ("\033[93mDifference = ", + diff)

    def display_prod(self, prod):
        print ("\033[93mProduct = ", + prod)

    def display_quot(self, quot):
        print ("\033[93mQuotient = ", + quot)

    def try_again(self):
        again = str(input("\n\033[90mDo you want to try again (YES or NO) ? "))
        return again
    
    def display_remainder(self, remainder):
        print ("\033[93mRemainder = ", + remainder)



    