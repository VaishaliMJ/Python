"""--------------------------------------------------------------------------------------------------
Problem Statement  :  Convert character list into String
Student Name       :  Vaishali Jorwekar           
-------------------------------------------------------------------------------------------------"""

#############################################################################################
#   Function Name   :   acceptCharactersInList
#   Input Params    :   -
#   Output Params   :   -
#   Description     :   Accept list elements from user.
#############################################################################################
def acceptNumbersInList():
    print(f"Enter characters in the list,Press '1' to stop accepting characters")
    charCount=0
    char=""
    charList=[]
    while char != ('1'):
        char=input(f"Character {charCount+1}:")
        
        if(char!='1'):
            charList.append((char))
        charCount+=1    
    return charList
#############################################################################################
#   Function Name   :   convertCharListToString
#   Input Params    :   charList
#   Output Params   :   -
#   Description     :   Convert to string
#############################################################################################
def convertCharListToString(charList):
    charString="".join(charList)
    print(f"Character list '{charList}' converted to string as  : {charString} and type :{type(charString)}")        
#############################################################################################
#   Function Name   :   main
#   Input Params    :   -
#   Output Params   :   -
#   Description     :   Calls other functions.
#############################################################################################
def main():
    #Accepts numbers in the list
    numberList=acceptNumbersInList()
    #Convert char list to String
    convertCharListToString(numberList)
#############################################################################################
#   Starter
#############################################################################################
if __name__=="__main__":
    main()