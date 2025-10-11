"""--------------------------------------------------------------------------------------------------
Problem Statement  :  Check for special characters in a string
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
#   Function Name   :   checkSpecialChars
#   Input Params    :   input String
#   Output Params   :   number(int)
#   Description     :   Count number of spaces,letters and digits in a string
#############################################################################################
def checkSpecialChars(inputString):
    specialChars=r"[^a-zA-Z0-9\s]"
    foundSpecialChars=re.findall(specialChars,inputString)
    return foundSpecialChars
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
    foundSpecialChars=checkSpecialChars(inputString)
    if len(foundSpecialChars)>1:
        print(f"String '{inputString}' contains special characters ...{foundSpecialChars}")
    else:
        print(f"String '{inputString}' does not contain any special characters...")
     
#############################################################################################
#   Starter
#############################################################################################
if __name__=="__main__":
    main()