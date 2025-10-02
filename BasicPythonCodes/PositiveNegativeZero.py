"""--------------------------------------------------------------------------------------------------
Problem Statement  :  Checks if number is Positive,Negative or Zero
Student Name       :  Vaishali Jorwekar           
-------------------------------------------------------------------------------------------------"""
#############################################################################################
#   imports
#############################################################################################

#############################################################################################
#   Function Name   :   postiveNegativeZero
#   Input Params    :   number(int)
#   Output Params   :   -
#   Description     :   Finds if number is Positive,Negative or Zero
#############################################################################################
def postiveNegativeZero(number:int):
    if number>0:
        print(f"{number} is  :'Postive'")
    elif number==0: 
        print(f"{number} is  :'Zero'")
    else:
        print(f"{number} is :'Negative'")    
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
    postiveNegativeZero(number)
#############################################################################################
#   Starter
#############################################################################################
if __name__=="__main__":
    main()