"""--------------------------------------------------------------------------------------------------
Problem Statement  :  
Student Name       :  Vaishali Jorwekar           
-------------------------------------------------------------------------------------------------"""
#############################################################################################
#   Function Name   :   acceptNumbers
#   Input Params    :   -
#   Output Params   :   number(int)
#   Description     :   Accepts number from user
#############################################################################################
def acceptNumbers():
    number1=int(input("Enter first Intger Number:"))
    number2=int(input("Enter second Intger Number:"))
    return number1,number2

#############################################################################################
#   Function Name   :   swapNumbers
#   Input Params    :   number1(int),number2(int)
#   Output Params   :   Swapped numbers 
#   Description     :   Swaps number without using third one
#############################################################################################
def swapNumbers(num1:int,num2:int):
    num2,num1=num1,num2
    print("Numbers after swapping:")
    print(f"Number 1 :{num1}")
    print(f"Number 2 :{num2}")
#############################################################################################
#   Function Name   :   main
#   Input Params    :   -
#   Output Params   :   -
#   Description     :   Calls other functions.
#############################################################################################
def main():
    num1,num2=acceptNumbers()
    swapNumbers(num1,num2)
    
#############################################################################################
#   Starter
#############################################################################################
if __name__=="__main__":
    main()