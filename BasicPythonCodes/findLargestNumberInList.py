"""--------------------------------------------------------------------------------------------------
Problem Statement  :  Find largest number from the list
Student Name       :  Vaishali Jorwekar           
-------------------------------------------------------------------------------------------------"""
BORDER="-"*59
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
#   Function Name   :   findLargestNum
#   Input Params    :   numList
#   Output Params   :   -
#   Description     :   finds largest number from list
#############################################################################################
def findLargestNum(numList):
   numList.sort(reverse=True)
   print(f"Largest number in the list {numList} is :{numList[0]}")      
#############################################################################################
#   Function Name   :   main
#   Input Params    :   -
#   Output Params   :   -
#   Description     :   Calls other functions.
#############################################################################################
def main():
    #Accepts numbers in the list
    print(BORDER)
    print("Enter first list elements:\n")
    print(BORDER)
    numList=acceptNumbersInList()
    print(BORDER)
    #find Largest number in the list
    findLargestNum(numList)
#############################################################################################
#   Starter
#############################################################################################
if __name__=="__main__":
    main()