"""--------------------------------------------------------------------------------------------------
Problem Statement  :  Reverse input string using silicing
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
#   Function Name   :   revStringUsingSlicing
#   Input Params    :   input String
#   Output Params   :   reversed String
#   Description     :   Reverse the given string
#############################################################################################
def revStringUsingSlicing(inputString):
    reversedString=inputString[::-1]
    return reversedString
#############################################################################################
#   Function Name   :   main
#   Input Params    :   -
#   Output Params   :   -
#   Description     :   Calls other functions.
#############################################################################################
def main():
    #Accept the string
    inputString=acceptString()
    #Reverse String using silicing
    revString=revStringUsingSlicing(inputString)
    print(f"Original String {inputString}  Reversed String :{revString}")
#############################################################################################
#   Starter
#############################################################################################
if __name__=="__main__":
    main()