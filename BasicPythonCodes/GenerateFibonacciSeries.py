"""--------------------------------------------------------------------------------------------------
Problem Statement  :  Generate Fibonacci series upto 'n' input number
Student Name       :  Vaishali Jorwekar           
-------------------------------------------------------------------------------------------------"""
#############################################################################################
#   Function Name   :   generateFibonacciSeries
#   Input Params    :   number(int)
#   Output Params   :   Returns fibonacci series upto 'number'
#   Description     :   Generate fibonacci series upto number 
#############################################################################################
def generateFibonacciSeries(number):
    if number<=0:
        return []
    elif number==1:
        return [0]
    else:
        fibSeries=[0,1]
        while len(fibSeries)<number:
            nextNum=fibSeries[-1]+fibSeries[-2]
            fibSeries.append(nextNum)
        return fibSeries    
#############################################################################################
#   Function Name   :   acceptNumber
#   Input Params    :   -
#   Output Params   :   number(int)
#   Description     :   Accepts number from user
#############################################################################################
def acceptNumber():
    number=int(input("Enter Intger Number:"))
    return number
#############################################################################################
#   Function Name   :   main
#   Input Params    :   -
#   Output Params   :   -
#   Description     :   Calls other functions.
#############################################################################################
def main():
    #Accept number from user
    number=acceptNumber()
    #Generate fibonacci series upto number 
    fibSeries=generateFibonacciSeries(number)
    print(f"Fibonacci Series upto '{number}' is : {', ' .join(str(element) for element in fibSeries)}")
#############################################################################################
#   Starter
#############################################################################################
if __name__=="__main__":
    main()