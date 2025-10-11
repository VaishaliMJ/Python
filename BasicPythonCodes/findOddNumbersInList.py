"""--------------------------------------------------------------------------------------------------
Problem Statement  :  Find ODD numbers from the list
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
#   Function Name   :   findOddNums
#   Input Params    :   list1
#   Output Params   :   -
#   Description     :   finds Odd numbers from list using list comprehension
#############################################################################################
def findOddNums(numList):
   oddNums=[number for number in numList if number%2!=0]
   print(f"Odd numbers in the list {numList} are :{oddNums}")      
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
    #find Odd numbers in the list
    findOddNums(numList)
#############################################################################################
#   Starter
#############################################################################################
if __name__=="__main__":
    main()