'''
By: Marcos Gil
Solution for this practice problem
https://practice.geeksforgeeks.org/problems/print-the-pattern-set-1/1
'''

'''
Name: printPattern
Purpose: Printing the pattern
 In: num = integer to generate pattern with
 In/Out: N/A
 Out: N/A
'''
def printPattern(num):
    count = num
    temp2 = num
    temp3 = num

    while temp3 != 0:

        temp = count

        while temp != 0:
            for i in range(0, temp2):
                print(temp, end = "")
            print()
            temp -= 1
        temp2 -= 1
        temp3 -= 1


def main():
    num = int(input("Please enter number to generate pattern from: "))
    printPattern(num)

main()
