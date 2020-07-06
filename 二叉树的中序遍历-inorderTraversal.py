class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list:
        res = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res

t1_1 = TreeNode(1)
t1_2 = TreeNode(2)
t1_3 = TreeNode(3)
t1_4 = TreeNode(4)
t1_5 = TreeNode(5)
t1_6 = TreeNode(6)
t1_7 = TreeNode(7)
t1_1.left = t1_2
t1_1.right = t1_3
t1_2.left = t1_4
t1_2.right = t1_5
t1_3.left = t1_6
t1_3.right = t1_7


t2_1 = TreeNode(1)
t2_2 = TreeNode(None)
t2_3 = TreeNode(2)
t2_4 = TreeNode(3)
t2_1.left = t2_2
t2_1.right = t2_3
t2_2.left = t2_4

print(Solution().inorderTraversal(t1_1))
print(Solution().inorderTraversal(t2_1))
