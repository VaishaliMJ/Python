"""--------------------------------------------------------------------------------------------------
Problem Statement  :  Add two lists
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
#   Function Name   :   addTwoLists
#   Input Params    :   list1,list2
#   Output Params   :   -
#   Description     :   Concat two list elements
#############################################################################################
def addTwoLists(list1,list2):
   resultList=[]
   for i in range(len(list1)):
        resultList.append(list1[i]+list2[i])
   print(f"Addition of lists {list1} and {list2} is :{resultList}")  
              
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
    list1=acceptNumbersInList()
    print(BORDER)
    print("Enter second list elements:\n")
    print(BORDER)
    list2=acceptNumbersInList()
    print("Second List Elements")
    #Add two list elements
    addTwoLists(list1,list2)
#############################################################################################
#   Starter
#############################################################################################
if __name__=="__main__":
    main()