"""--------------------------------------------------------------------------------------------------
Problem Statement  :  Check for Palindrome string using silicing
Student Name       :  Vaishali Jorwekar           
-------------------------------------------------------------------------------------------------"""
#############################################################################################
#   Function Name   :   acceptString
#   Input Params    :   -
#   Output Params   :   accepted input string
#   Description     :   Accepts String from user
#############################################################################################
def acceptString():
    inputString=input("Enter input String:")
    return inputString  
#############################################################################################
#   Function Name   :   checkPalindrome
#   Input Params    :   input String
#   Output Params   :   number(int)
#   Description     :   Accepts String from user
#############################################################################################
def checkPalindrome(inputString):
    reversedString=inputString[::-1]
    print(f"Original String {inputString}  Reversed String :{reversedString}")

    if(inputString==reversedString):
        print(f"String '{inputString}' is Palindrome ")
    else:
        print(f"String '{inputString}' is not Palindrome ")
#############################################################################################
#   Function Name   :   main
#   Input Params    :   -
#   Output Params   :   -
#   Description     :   Calls other functions.
#############################################################################################
def main():
    #Accept the string
    inputString=acceptString()
    #Check for Palindrome using silicing
    checkPalindrome(inputString)
#############################################################################################
#   Starter
#############################################################################################
if __name__=="__main__":
    main()