'''
By: Marcos Gil
Solution for this practice problem
https://practice.geeksforgeeks.org/problems/print-alternate-elements-of-an-array/1
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

def alternatePrint(list):
    print("The alternate printing of", list, "is:", end = " ")

    for i in range(0, len(list), 2):
        print(list[i], end = " ")
    print()

def main():
    list = getList()
    alternatePrint(list)

main()
