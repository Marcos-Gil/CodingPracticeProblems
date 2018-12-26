'''
By: Marcos Gil
Solution for this practice problem
https://practice.geeksforgeeks.org/problems/searching-a-number/0
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
Name: linearSearch
Purpose: Search list for a specific value
 In: list = list of integer values
     target = integer we are searching for
 In/Out: N/A
 Out: int = index of target (-1 if not found)
'''
def linearSearch(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return -1

def main():
    list = getList()
    target = int(input("Number to search list for: "))
    index = linearSearch(list, target)

    if index == -1:
        print(target, "not found in", list)
    else:
        print(target, "is at index", index, "in the list", list)

main()
