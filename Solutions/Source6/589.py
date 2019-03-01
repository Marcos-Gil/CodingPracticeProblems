"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        values = []

        def traverse(root, nodes):
            if root:
                values.append(root.val)
                for child in root.children:
                    traverse(child, nodes)

        traverse(root, values)

        return values
asdg
