"""--------------------------------------------------------------------------------------------------
Problem Statement  :  Count white spaces in a string
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
#   Function Name   :   countWhiteSpaces
#   Input Params    :   input String
#   Output Params   :   number(int)
#   Description     :   Count number of spaces in a string
#############################################################################################
def countWhiteSpaces(inputString):
    whiteSpaceCnt=inputString.count(" ")
    print(f"Number of white/Empty spaces in '{inputString}' are : {whiteSpaceCnt}")
#############################################################################################
#   Function Name   :   main
#   Input Params    :   -
#   Output Params   :   -
#   Description     :   Calls other functions.
#############################################################################################
def main():
    #Accept the string
    inputString=acceptString()
    #Count white spaces in a string
    countWhiteSpaces(inputString)
#############################################################################################
#   Starter
#############################################################################################
if __name__=="__main__":
    main()