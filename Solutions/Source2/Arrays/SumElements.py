'''
By: Marcos Gil
Solution for this practice problem
https://practice.geeksforgeeks.org/problems/sum-of-array-elements/0
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
Name: sumList
Purpose: Sum all of the values in the list
 In: list = list of integer values
 In/Out: N/A
 Out: totalSum = sum of all list elements
'''
def sumList(list):
    totalSum = 0;

    for i in range(0, len(list)):
        totalSum = totalSum + list[i]

    return totalSum

def main():
    list = getList()
    result = sumList(list)
    print("The total sum of the list elements is", result)

main()
