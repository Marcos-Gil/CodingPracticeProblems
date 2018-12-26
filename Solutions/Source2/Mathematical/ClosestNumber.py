'''
By: Marcos Gil
Solution for this practice problem
https://practice.geeksforgeeks.org/problems/closest-number/0
'''

'''
Name: closestNum
Purpose: Find number closest to N divisible by M
 In: values = list containg N and M
 In/Out: N/A
 Out: int = closest number to N divisible by M
'''
def closestNum(values):
    if values[0] < 0:
        closest = values[0] - 1
        while (closest % values[1] != 0):
            closest -= 1
        values[2] = closest
        return values[2]
    else:
        closest = values[0] - 1
        while (closest > 0):
            if closest % values[1] == 0:
                values[2] = closest
                return values[2]
            closest -= 1

'''
Name: getValues
Purpose: Getting values for N and M from the user
 In: N/A
 In/Out: N/A
 Out: list = values with N and M
'''
def getValues():
    values = []
    values.append(int(input("Please enter the value of N: ")))
    values.append(int(input("Please enter the value of M: ")))
    values.append(-99999)
    return values

def main():
    values = getValues()
    closest = closestNum(values)
    print(closest)

main()
