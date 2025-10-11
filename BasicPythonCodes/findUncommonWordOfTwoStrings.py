"""--------------------------------------------------------------------------------------------------
Problem Statement  :  Find Uncommon Words of Two Strings
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
#   Function Name   :   uncommon_words
#   Input Params    :   firstString,secondString
#   Output Params   :   -
#   Description     :   Finds uncommon words from both the strings
#   Author          :   Vaishali Jorwekar
#   Date            :   3 Oct 2025
#############################################################################################
def find_uncommon_words(firstString:str,secondString:str):
    # Split the string into words
    firstStringWords=set(firstString.split())
    secondStringWords=set(secondString.split())
    #uncommon words,use set difference
    uncommonWords=firstStringWords.symmetric_difference(secondStringWords)
    #Convert set elements into list again
    uncommonWordList=list(uncommonWords)
    return uncommonWordList
#############################################################################################
#   Function Name   :   main
#   Input Params    :   -
#   Output Params   :   -
#   Description     :   Calls other functions.
#############################################################################################
def main():
    # First String
    firstString=acceptString()
    # Second String
    secondString=acceptString()
    # Find Uncommon words
    uncommonWordList=find_uncommon_words(firstString,secondString)
    print(f"Uncommon words in the '{firstString}'  and '{secondString}' are:\n{uncommonWordList}")

#############################################################################################
#   Starter
#############################################################################################
if __name__=="__main__":
    main()