"""--------------------------------------------------------------------------------------------------
Problem Statement  :  Even or odd
Student Name       :  Vaishali Jorwekar           
-------------------------------------------------------------------------------------------------"""
#############################################################################################
#   imports
#############################################################################################

#############################################################################################
#   Function Name   :   EvenOdd
#   Input Params    :   number(int)
#   Output Params   :   -
#   Description     :   Finds if number is Even or odd
#############################################################################################
def EvenOdd(number:int):
    if number%2==0:
        print(f"{number} is an Even Number")
    else:
        print(f"{number} is an Odd Number")    
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
    #Finds if given number Even or Odd
    EvenOdd(number)
#############################################################################################
#   Starter
#############################################################################################
if __name__=="__main__":
    main()