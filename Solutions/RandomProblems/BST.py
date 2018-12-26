nums = []
for i in range(0, 2000000):
    nums.append(i)
index = None
left = 0
right = len(nums) - 1
found = False
target = int(input("What value do you want to search for? "))

while (right >= left):

    mid = left + (right - left) // 2
    print(mid)

    if nums[mid] == target:
        found = True
        index = mid
        break
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

if not found:
    print(target, "not found")
else:
    print(target, "found at position", index)











# def rotate(nums, k):
#     """
#     :type nums: List[int]
#     :type k: int
#     :rtype: void Do not return anything, modify nums in-place instead.
#     """
    # numList = nums[:]
    # print("lol",numList)
    #
    # if k == 0: # if no rotation nothing to do
    #     return
    #
    # nums.append(numList[len(nums) - k:len(nums)])
    # print(nums)
    # nums.append(numList[0:len(nums) - k])
    # print(nums)
    # nums[:] = nums.append(numList[len(nums) - k:len(nums)]) + nums.append(numList[0:len(nums) - k])
#
# def lengthOfLongestSubstring(s):
#         """
#         :type s: str
#         :rtype: int
#         """
#
#         if len(s) == 1:
#             return 1
#
#         allKeys = {}
#         currentSub = 0
#         longest = 0
#
#         i = 0
#
#         while i < len(s):
#             if s[i] not in allKeys:
#                 allKeys[s[i]] = i
#                 currentSub += 1
#                 if i == len(s) - 1:
#                     if currentSub > longest:
#                         longest = currentSub
#                         break
#                 i += 1
#             else:
#                 lastSubBeforeDup = i - allKeys[s[i]] - 1
#                 print("allKeys[s[",i,"]] =", allKeys[s[i]])
#                 if currentSub > longest:
#                     longest = currentSub
#                 currentSub = lastSubBeforeDup
#                 allKeys.pop(s[i])
#                 print(allKeys)
#
#         return longest
#         "datgvdfipl"
# def main():
#     s = "abba"
#     print(lengthOfLongestSubstring(s))
#
# main()
