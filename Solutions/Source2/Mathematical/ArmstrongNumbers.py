'''
By: Marcos Gil
Solution for this practice problem
https://practice.geeksforgeeks.org/problems/armstrong-numbers/0
'''

'''
Name: checkArmstrong
Purpose: Check if the number is an armstrong number
 In: nums = number to check
 In/Out: N/A
 Out: boolean = true if number is armstrong number, false otherwise
'''
def checkArmstrong(nums):
    originalNum = int(nums)
    sumOfCubeDigits = 0;

    numList = [int(x) for x in nums]

    for x in numList:
        sumOfCubeDigits = sumOfCubeDigits + x**3

    if sumOfCubeDigits == originalNum:
        return True
    else:
        return False

def main():
    numToCheck = input("Please enter the potential 3-digit Armstrong Number: ")
    isArmstrong = checkArmstrong(numToCheck)

    if isArmstrong:
        print(numToCheck, "is an Armstrong Number!")
    else:
        print(numToCheck, "is not an Armstrong Number!")

main()
