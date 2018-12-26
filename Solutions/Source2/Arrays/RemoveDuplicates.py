'''
By: Marcos Gil
Solution for this practice problem
https://practice.geeksforgeeks.org/problems/remove-duplicate-elements-from-sorted-array/1
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
Name: removeDuplicates
Purpose: Remove duplicates from the list and return length of new list
 In: list = list of integers
 In/Out: N/A
 Out: currentLen = integer length of list after removals
'''
def removeDuplicates(nums):
    dict = {}
    currentLen = len(nums) # will remove 1 from this for every duplicate
    indexToDelete = [] # storing indexes of the values we need to delete

    for i in range(0, len(nums)):
        if nums[i] in dict:
            dict[nums[i]] += 1
            indexToDelete.append(i)
            currentLen -= 1
        else:
            dict[nums[i]] = 1

    for j in range(len(indexToDelete) - 1, -1, -1): # delete from back to front so indexes remain accurate
        del nums[indexToDelete[j]]

    return currentLen

def main():
    numbers = getList()
    print("The list before duplicate removal is:", numbers)
    print("The length is:", len(numbers))
    length = removeDuplicates(numbers)
    print("The list after duplicate removal is:", numbers)
    print("The length is:", length)

main()
