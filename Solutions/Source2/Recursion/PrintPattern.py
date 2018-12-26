'''
By: Marcos Gil
Solution for this practice problem
https://practice.geeksforgeeks.org/problems/print-pattern/0
'''
def printPattern(num):
    if num <= 0:
        print(num, end = " ")
    else:
        print(num, end = " ")
        printPattern(num - 5)
        print(num, end = " ")

def main():
    num = int(input("Please enter the number to generate the pattern from: "))
    printPattern(num)

main()
