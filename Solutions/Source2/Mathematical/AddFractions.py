'''
By: Marcos Gil
Solution for this practice problem
https://practice.geeksforgeeks.org/problems/add-two-fractions/1
'''

'''
Name: addFractions
Purpose: Add two fractions
 In: fractions = list of fraction values
 In/Out: N/A
 Out: finalFraction = list with final fraction values
'''
def addFractions(fractions):
    finalFraction = []

    if fractions[1] == fractions[3]:
        finalFraction.append(fractions[0] + fractions[2])
        finalFraction.append(fractions[1])
        return finalFraction
    else:
        finalFraction.append((fractions[0] * fractions[3]) + (fractions[1] * fractions[2]))
        finalFraction.append(fractions[1] * fractions[3])
        return finalFraction

'''
Name: getFractions
Purpose: Get fraction values from the user
 In: N/A
 In/Out: N/A
 Out: fractionValues = list of fraction values
'''
def getFractions():
    fractionValues = []
    print("You will now enter the values for the fractions to add")
    fractionValues.append(int(input("Numerator of first fraction: ")))
    fractionValues.append(int(input("Denoninator of the first fraction: ")))
    fractionValues.append(int(input("Numerator of second fraction: ")))
    fractionValues.append(int(input("Denominator of second fraction: ")))
    return fractionValues

'''
Name: printAnswer
Purpose: Print solution of fraction addition
 In: fractions = list of original fractions added
     solution = result of adding fractions
 In/Out: N/A
 Out: N/A
'''
def printAnswer(fractions, solution):
    print("Adding fractions:")
    print(fractions[0], " ", fractions[2])
    print("- + -")
    print(fractions[1], " ", fractions[3])
    print("The solution is:")
    print(solution[0])
    print("-")
    print(solution[1])

def main():
    fractions = getFractions()
    answer = addFractions(fractions)
    printAnswer(fractions, answer)

main()
