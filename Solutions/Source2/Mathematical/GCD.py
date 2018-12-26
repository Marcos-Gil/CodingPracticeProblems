'''
By: Marcos Gil
Solution for this practice problem
https://practice.geeksforgeeks.org/problems/gcd-of-two-numbers/0
'''

'''
Name: computeGCD
Purpose: Compute GCD of two numbers
 In: num1 = first integer
     num2 = second integer
 In/Out: N/A
 Out: int = gcd value
'''
def computeGCD(num1, num2):
    if num2 == 0:
        return num1
    return computeGCD(num2, num1 % num2)

def main():
    print("Computing the GCD of two numbers.")
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))
    gcd = computeGCD(num1, num2)
    print("The GCD is", gcd)

main()
