# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        values = []

        def traverse(root, values): # helper function
            """
            :type root: TreeNode
            :type values: List[int]
            :rtype: List[int]
            """
            if root: # if node we are at exists, continue to do in order traversal
                traverse(root.left, values)
                values.append(root.val)
                traverse(root.right, values)

        traverse(root, values)

        return values
ads
