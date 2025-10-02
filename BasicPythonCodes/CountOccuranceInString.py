"""--------------------------------------------------------------------------------------------------
Problem Statement  :  Count number of chracter occurance in a String
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
#   Function Name   :   countCharOccurance
#   Input Params    :   inputString,inputChar
#   Output Params   :   -
#   Description     :   Count number of occurances of 'inputChar' in input string
#############################################################################################
def countCharOccurance(inputString,inputChar):
    #counter for character
    charCount=0
    for inChar in inputString:
        if inChar==inputChar:
            charCount+=1
    print(f"Character '{inputChar}' occured in '{inputString}': {charCount} times")        

#############################################################################################
#   Function Name   :   main
#   Input Params    :   -
#   Output Params   :   -
#   Description     :   Calls other functions.
#############################################################################################
def main():
    #Accepts input string from user
    inputString=acceptString()
    #Accept character from the user
    print("Accepting charcter from user:")
    inputChar=acceptString()
    #count character ocurance from the string
    countCharOccurance(inputString,inputChar)
    
#############################################################################################
#   Starter
#############################################################################################
if __name__=="__main__":
    main()