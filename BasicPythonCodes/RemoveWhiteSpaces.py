"""--------------------------------------------------------------------------------------------------
Problem Statement  :  Remove white spaces in a string
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
#   Function Name   :   removeWhiteSpaces
#   Input Params    :   input String
#   Output Params   :   -
#   Description     :   Remove spaces in a string
#############################################################################################
def removeWhiteSpaces(inputString):
    spaces=re.compile(r'\s+')
    updatedString=re.sub(spaces,"",inputString)
    print(f"Input string with white/Empty spaces '{inputString}' ,Updated String : {updatedString}")
#############################################################################################
#   Function Name   :   main
#   Input Params    :   -
#   Output Params   :   -
#   Description     :   Calls other functions.
#############################################################################################
def main():
    #Accept the string
    inputString=acceptString()
    #Remove white spaces in a string
    removeWhiteSpaces(inputString)
#############################################################################################
#   Starter
#############################################################################################
if __name__=="__main__":
    main()