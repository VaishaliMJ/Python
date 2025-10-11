"""--------------------------------------------------------------------------------------------------
Problem Statement  :  Find Second largest number from the list
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
#   Function Name   :   findSecondLargestNum
#   Input Params    :   numList
#   Output Params   :   -
#   Description     :   finds largest number from list
#############################################################################################
def findSecondLargestNum(numList):
   numList.sort(reverse=True)
   
   if(len(numList)>=2):
       secondLargest=numList[1]
       print(f"Second Largest number in the list {numList} is :{secondLargest}")  
   else:
      print(f"List {numList} does not contain second largest element")  
        
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
    #find second Largest number in the list
    findSecondLargestNum(numList)
#############################################################################################
#   Starter
#############################################################################################
if __name__=="__main__":
    main()