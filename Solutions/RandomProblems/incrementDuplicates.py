'''
By: Marcos Gil
Solution for StackOverflow Question:
    Given an array, we want it to make it unique by incrementing any duplicate elements in array such
    that the sum of array unique elements is minimal. In other words, if two or more elements in array are
    not unique, we must increase the value of the duplicate element(s) to some other number(s) such that
    array consists of unique elements that sum to a number that is as small as possible.
'''
def incDup(list):
    dict = {}
    j = 0
    while j < len(list):
        if list[j] in dict: # if value has been seen, we keep increasing it
            list[j] += 1
        else: # first time seeing value
            dict[list[j]] = 1
            j += 1

    print(list)

def main():
    incDup([3,2,2,7,7])
    incDup([3,2,1,7,7])

main()
