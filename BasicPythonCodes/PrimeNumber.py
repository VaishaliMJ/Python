"""--------------------------------------------------------------------------------------------------
Problem Statement  :  Find if number is Prime
Student Name       :  Vaishali Jorwekar           
-------------------------------------------------------------------------------------------------"""
#############################################################################################
#   imports
#############################################################################################

#############################################################################################
#   Function Name   :   checkPrime
#   Input Params    :   number(int)
#   Output Params   :   -
#   Description     :   Finds if number is Prime
#############################################################################################
def checkPrime(number:int):
    flag=False
    if number==1:
        flag=True
    elif number > 1:
            for cnt in range(2,number):
                 if number % cnt==0:
                      flag=True
                      break
    if flag:
        print(f"{number} is not a Prime Number...")  
    else:
        print(f"{number} is a Prime Number...")  
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
    #Finds if given number is Prime
    checkPrime(number)
#############################################################################################
#   Starter
#############################################################################################
if __name__=="__main__":
    main()