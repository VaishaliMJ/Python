"""--------------------------------------------------------------------------------------------------
Problem Statement  :  Find the minimum number from the list
Student Name       :  Vaishali Jorwekar           
-------------------------------------------------------------------------------------------------"""

#############################################################################################
#   Function Name   :   acceptNumbersInList
#   Input Params    :   -
#   Output Params   :   -
#   Description     :   Accept list elements from user.
#############################################################################################
def acceptNumbersInList():
    print(f"Enter numbers in the list,Press 'q' to stop accepting numbers")
    numCount=0
    number=""
    inputNumbers=[]
    while number != ('q'.lower()):
        number=input(f"Number {numCount+1}:")
        
        if(number!='q'):
            inputNumbers.append(int(number))
        numCount+=1    
    return inputNumbers
#############################################################################################
#   Function Name   :   findMinimumNumberInList
#   Input Params    :   numberList
#   Output Params   :   -
#   Description     :   Finds Maximum number from the list.
#############################################################################################
def findMinimumNumberInList(numberList):
    min=numberList[0]
    for num in numberList:
        if num < min:
            min=num
    print(f"Minimum number in list '{numberList}' is  : {min}")        
#############################################################################################
#   Function Name   :   main
#   Input Params    :   -
#   Output Params   :   -
#   Description     :   Calls other functions.
#############################################################################################
def main():
    #Accepts numbers in the list
    numberList=acceptNumbersInList()
    #Minimum number from the list
    findMinimumNumberInList(numberList)
#############################################################################################
#   Starter
#############################################################################################
if __name__=="__main__":
    main()