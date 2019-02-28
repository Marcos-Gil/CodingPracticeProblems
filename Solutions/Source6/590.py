"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        values = []

        def traverse(root, nodes):
            if root:
                for child in root.children:
                    traverse(child, nodes)
                values.append(root.val)

        traverse(root, values)

        return values
asd
