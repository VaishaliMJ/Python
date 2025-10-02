"""--------------------------------------------------------------------------------------------------
Problem Statement  :  Count number of vowels in a string
Student Name       :  Vaishali Jorwekar           
-------------------------------------------------------------------------------------------------"""
#############################################################################################
#   Constants
#############################################################################################
VOWELS=['a','e','i','o','u']
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
#   Function Name   :   countVowels
#   Input Params    :   inputString
#   Output Params   :   -
#   Description     :   Count number of vowels in input string
#############################################################################################
def countVowels(inputString):
    #counter for vowels
    vowelCount=0
    for inChar in inputString.lower():
        if inChar in VOWELS:
            vowelCount+=1
    print(f"Number of vowels in '{inputString} are : {vowelCount}")        

#############################################################################################
#   Function Name   :   main
#   Input Params    :   -
#   Output Params   :   -
#   Description     :   Calls other functions.
#############################################################################################
def main():
    #Accepts input string from user
    inputString=acceptString()
    #count vowels from the string
    countVowels(inputString)
    
#############################################################################################
#   Starter
#############################################################################################
if __name__=="__main__":
    main()