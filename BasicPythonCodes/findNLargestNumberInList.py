"""--------------------------------------------------------------------------------------------------
Problem Statement  :  Find 'n' largest number from the list
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
#   Function Name   :   findNLargestNums
#   Input Params    :   numList
#   Output Params   :   -
#   Description     :   finds largest number from list
#############################################################################################
def findNLargestNums(numList,nums):
   numList.sort(reverse=True)
   
   if(len(numList)>=nums):
       largestN_Nums=numList[:nums]
       print(f"N Largest number in the list {numList} is :{largestN_Nums}")  
   else:
      print(f"List {numList} does not contain {nums} largest elements")  
        
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
    num=int(input("Enter how many largest numbers to find:"))
    #find n Largest number in the list
    findNLargestNums(numList,num)
#############################################################################################
#   Starter
#############################################################################################
if __name__=="__main__":
    main()