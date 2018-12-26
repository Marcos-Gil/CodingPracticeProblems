'''
By: Marcos Gil
Solution for this practice problem
https://practice.geeksforgeeks.org/problems/second-largest/0
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
Name: secondLargest
Purpose: Find second largest value in list
 In: list = list of values
 In/Out: N/A
 Out: int = second largest value in list
'''
def secondLargest(list):
    largest = -9999999999999
    secondLargest = -9999999999999

    for i in range(0, len(list)):
        if list[i] > largest:
            secondLargest = largest
            largest = list[i]
        elif list[i] > secondLargest and list[i] != largest:
            secondLargest = list[i]

    return secondLargest

def main():
    list = getList()
    result = secondLargest(list)
    if (len(list) < 2):
        print("Not enough values entered.")
    else:
        print("The second largest value in", list, "is", result)

main()
