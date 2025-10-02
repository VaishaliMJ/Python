"""--------------------------------------------------------------------------------------------------
Problem Statement  :  Intger To Decimal
Student Name       :  Vaishali Jorwekar           
-------------------------------------------------------------------------------------------------"""
#############################################################################################
#   imports
#############################################################################################
import decimal
#############################################################################################
#   Function Name   :   intgerToDecimal
#   Input Params    :   number(int)
#   Output Params   :   -
#   Description     :   Convert integer to decimal number
#############################################################################################
def intgerToDecimal(number):
    print(decimal.Decimal(number))
    print(type(decimal.Decimal(number)))    
#############################################################################################
#   Function Name   :   acceptNumber
#   Input Params    :   -
#   Output Params   :   number(int)
#   Description     :   Accepts number from user
#############################################################################################
def acceptNumber():
    number=int(input("Enter Intger Number:"))
    return number
#############################################################################################
#   Function Name   :   main
#   Input Params    :   -
#   Output Params   :   -
#   Description     :   Calls other functions.
#############################################################################################
def main():
    #Accept number from user
    number=acceptNumber()
    #Converts to decimal number
    intgerToDecimal(number)
#############################################################################################
#   Starter
#############################################################################################
if __name__=="__main__":
    main()