"""--------------------------------------------------------------------------------------------------
Problem Statement  :  Count special characters in a string
Student Name       :  Vaishali Jorwekar           
-------------------------------------------------------------------------------------------------"""
import re
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
#   Function Name   :   countSpecialChars
#   Input Params    :   input String
#   Output Params   :   number(int)
#   Description     :   Count number of spaces,letters and digits in a string
#############################################################################################
def countSpecialChars(inputString):
    specialChars="!@$#%^&*()_/\<>[]{}:;~`?"
    specialCharCount=0
    for char in inputString:
        if char in specialChars:
            specialCharCount+=1
    print(f"Number of special characters in {inputString} are :{specialCharCount}")     
#############################################################################################
#   Function Name   :   main
#   Input Params    :   -
#   Output Params   :   -
#   Description     :   Calls other functions.
#############################################################################################
def main():
    #Accept the string
    inputString=acceptString()
    #Count special characters in a string
    countSpecialChars(inputString)
#############################################################################################
#   Starter
#############################################################################################
if __name__=="__main__":
    main()