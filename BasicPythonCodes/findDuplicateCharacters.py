"""--------------------------------------------------------------------------------------------------
Problem Statement  :  Find Duplicate characters in the String
Student Name       :  Vaishali Jorwekar           
-------------------------------------------------------------------------------------------------"""
#############################################################################################
#   Function Name   :   acceptString
#   Input Params    :   -
#   Output Params   :   accepted input string
#   Description     :   Accepts String from user
#   Author          :   Vaishali Jorwekar
#   Date            :   3 Oct 2025
#############################################################################################
def acceptString():
    inputString=input("Enter input String:")
    return inputString  
#############################################################################################
#   Function Name   :   findDuplicateCharacters
#   Input Params    :   inputString
#   Output Params   :   -
#   Description     :   Finds duplicate characters from the string
#   Author          :   Vaishali Jorwekar
#   Date            :   3 Oct 2025
#############################################################################################
def findDuplicateCharacters(inputString:str):
    # Dictionary to store character count
    char_list=dict()
    # Duplicate char list
    duplicates=[]

    for char in inputString:
        if char in char_list:
            char_list[char]+=1
        else:
            char_list[char]=1

    for char,charCount in char_list.items():
        if charCount > 1:
            duplicates.append(char) 
    return duplicates               
#############################################################################################
#   Function Name   :   main
#   Input Params    :   -
#   Output Params   :   -
#   Description     :   Calls other functions.
#############################################################################################
def main():
    # input  String
    inputString=acceptString()
    duplicateCharsList=findDuplicateCharacters(inputString)
    print(f"Duplicate characters in the '{inputString}' are:\n{duplicateCharsList}")

#############################################################################################
#   Starter
#############################################################################################
if __name__=="__main__":
    main()