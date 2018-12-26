'''
By: Marcos Gil
Solution for this practice problem
https://practice.geeksforgeeks.org/problems/print-table/0
'''

'''
Name: createTable
Purpose: Print table of N up to 10
 In: num = value of N
 In/Out: N/A
 Out: N/A
'''
def createTable(num):
    for i in range (1, 11):
        print(i * num, end = " ")
    print()

def main():
    userNum = int(input("Please enter value to create table from: "))
    createTable(userNum)

main()
