'''
By: Marcos Gil
Solution for this practice problem
https://practice.geeksforgeeks.org/problems/check-if-an-array-is-sorted/0
'''

'''
Name: getList
Purpose: Get values for list from the user
 In: N/A
 In/Out: N/A
 Out: list = list of values as integers
'''
def getList():
    userValues = input("Enter space seperated numbers as list values: ").split(" ")
    list = [int(x) for x in userValues]
    return list

'''
Name: checkSorted
Purpose: Check if the list is sorted in ascending order
 In: list = list of values as integers
 In/Out: N/A
 Out: boolean = if sorted or not
'''
def checkSorted(list):
    for i in range (0, len(list) - 1):
        if list[i] > list[i + 1]:
            return False
    return True

'''
Name: printResult
Purpose: Print the result
 In: bool = boolean if list is sorted or not,
     list = the list of values
 In/Out: N/A
 Out: N/A
'''
def printResult(bool, list):
    if bool == True:
        print("The list:", list, "is sorted in ascending order.")
    else:
        print("The list:", list, "is not sorted in ascending order.")

def main():
    list = getList()
    isSorted = checkSorted(list)
    printResult(isSorted, list)

main()
