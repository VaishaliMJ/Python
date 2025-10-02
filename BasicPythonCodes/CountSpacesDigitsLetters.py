"""--------------------------------------------------------------------------------------------------
Problem Statement  :  Count white spaces,Letters and digits in a string
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
#   Function Name   :   countSpacesDigitsLetters
#   Input Params    :   input String
#   Output Params   :   number(int)
#   Description     :   Count number of spaces,letters and digits in a string
#############################################################################################
def countSpacesDigitsLetters(inputString):

    letterCount=re.findall("[a-zA-Z]",inputString)
    digitCount=re.findall("[0-9]",inputString)
    spaceCount=re.findall(r"[\s]",inputString)
    print(f"Input String {inputString} \
          \n\tWhite/Empty spaces: {len(spaceCount)}\
          \n\tLetter count :{len(letterCount)}\
          \n\tDigit Count:{(len(digitCount))}")
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
    countSpacesDigitsLetters(inputString)
#############################################################################################
#   Starter
#############################################################################################
if __name__=="__main__":
    main()