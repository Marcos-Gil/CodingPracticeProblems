'''
By: Marcos Gil
Solution for this practice problem
https://practice.geeksforgeeks.org/problems/reverse-an-array/0
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
Name: printReverse
Purpose: Print list values in reverse
 In: list = list of integer values
 In/Out: N/A
 Out: N/A
'''
def printReverse(list):
    print("The reverse is:", end = " ")
    for i in range (len(list), 0, -1):
        print(list[i - 1], end = " ")
    print()

def main():
    list = getList()
    printReverse(list)

main()
