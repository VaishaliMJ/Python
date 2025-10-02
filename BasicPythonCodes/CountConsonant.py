"""--------------------------------------------------------------------------------------------------
Problem Statement  :  Count number of consonant in a string
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
#   Function Name   :   countConsonant
#   Input Params    :   inputString
#   Output Params   :   -
#   Description     :   Count number of consonant in input string
#############################################################################################
def countConsonant(inputString):
    #counter for consonant
    consonantCount=0
    for inChar in inputString.lower():
        if inChar not in VOWELS:
            if not (inChar==" " or inChar=="\t"):
                consonantCount+=1
    print(f"Number of vowels in '{inputString}' are : {consonantCount}")        

#############################################################################################
#   Function Name   :   main
#   Input Params    :   -
#   Output Params   :   -
#   Description     :   Calls other functions.
#############################################################################################
def main():
    #Accepts input string from user
    inputString=acceptString()
    #count consonant from the string
    countConsonant(inputString)
    
#############################################################################################
#   Starter
#############################################################################################
if __name__=="__main__":
    main()