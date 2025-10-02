"""--------------------------------------------------------------------------------------------------
Problem Statement  :  Print a star (*) pattern
Student Name       :  Vaishali Jorwekar    
            *
        *       *
    *               *
*                       *   
    *               *
        *       *
            *
-------------------------------------------------------------------------------------------------"""
#############################################################################################
#   constants
#############################################################################################
STAR="*"
#############################################################################################
#   Function Name   :   printStarPattern
#   Input Params    :   row(int),col(int)
#   Output Params   :   -
#   Description     :   Print given * pattern
#############################################################################################
def printStarPattern(row,col):
    if row!=col:
        print("Invalid Input...Enter same number of rows n cols")
        return
    for r in range(1,row+1):
        for c in range(col-r):
            print(" ",end="\t")
        for c in range(1,2*r): 
            if c==1 or c==2*r-1:   
                print(STAR,end="\t")
            else:
                print(" ",end="\t")    
        print("\n")

    for r in range(row-1,0,-1):
        for c in range(col-r):
            print(" ",end="\t")
        for c in range(1,2*r): 
            if c==1 or c==2*r-1:   
                print(STAR,end="\t")
            else:
                print(" ",end="\t")    
        print("\n")
      
#############################################################################################
#   Function Name   :   acceptRowCols
#   Input Params    :   -
#   Output Params   :   row(int),col(int)
#   Description     :   Accepts number from user 
#############################################################################################
def acceptRowCols():
    row=int(input("Enter number of rows:"))
    col=int(input("Enter number of columns:"))
    return row,col
#############################################################################################
#   Function Name   :   main
#   Input Params    :   -
#   Output Params   :   -
#   Description     :   Calls other functions.
#############################################################################################
def main():
    #Accept number from user in string format
    rows,cols=acceptRowCols()
    #prints star pattern
    printStarPattern(rows,cols)
#############################################################################################
#   Starter
#############################################################################################
if __name__=="__main__":
    main()