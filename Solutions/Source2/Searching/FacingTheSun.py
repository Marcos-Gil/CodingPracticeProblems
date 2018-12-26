'''
By: Marcos Gil
Solution for this practice problem
https://practice.geeksforgeeks.org/problems/facing-the-sun/0
'''

'''
Name: printResult
Purpose: Print the result
 In: inSun = int for buildings in sun,
     buildingList = list of building heights
 In/Out: N/A
 Out: N/A
'''
def printResult(inSun, buildingList):
    if inSun < 0:
        print("Empty list was entered")
    else:
        print("The buildings are:", buildingList)
        print("There are", inSun, "buildings receiving sunlight.")

'''
Name: getList
Purpose: Get building heights from user as a list
 In: N/A
 In/Out: N/A
 Out: list = list of building heights
'''
def getList():
    userValues = input("Enter space seperated digits as building height values: ").split(" ")
    list = [int(x) for x in userValues]
    return list

'''
Name: amountInSun
Purpose: Calculate the amount of buildings in the sun
 In: buildings = list of building heights
 In/Out: N/A
 Out: numFacingSun = int value of buildings in sun
'''
def amountInSun(buildings):
    if (len(buildings) == 0):
        return -1
    else:
        numFacingSun = 1
        lastHeight = buildings[0]

        for i in range (1, len(buildings)):
            if buildings[i] > lastHeight:
                numFacingSun += 1
                lastHeight = buildings[i]

        return numFacingSun

def main():
    buildings = getList()
    inSun = amountInSun(buildings)
    printResult(inSun, buildings)

main()
