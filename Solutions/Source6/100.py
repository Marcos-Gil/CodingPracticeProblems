# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # store nodes from each tree
        nodesTreeOne = []
        nodesTreeTwo = []

        # pre order traversal of tree helper function
        def preOrder(root, nodes):
            if root:
                nodes.append(root.val)
                preOrder(root.left, nodes)
                preOrder(root.right, nodes)
            else:
                nodes.append(None)

        # traverse both trees
        preOrder(p, nodesTreeOne)
        preOrder(q, nodesTreeTwo)

        # if nodes are equal or not
        if nodesTreeOne == nodesTreeTwo:
            return True
        else:
            return False
