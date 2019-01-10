# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []

        stack.append(root)
        stack.append(root)

        while len(stack) != 0:
            tree1 = stack.pop()
            tree2 = stack.pop()
            if tree1 == None and tree2 == None:
                continue
            if tree1 == None or tree2 == None:
                return False
            if tree1.val != tree2.val:
                return False
            stack.append(tree1.left)
            stack.append(tree2.right)
            stack.append(tree1.right)
            stack.append(tree2.left)

        return True
