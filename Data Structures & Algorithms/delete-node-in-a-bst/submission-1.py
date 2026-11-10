# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def helper(root, key):
            

            #find the root we need to delete
            if not root:
                return None

            if root.val < key:
                root.right = helper(root.right, key)
            
            elif root.val > key:
                root.left = helper(root.left , key)


            else:
                if not root.left:
                    return root.right

                if not root.right:
                    return root.left


                cur = root.right
                while cur.left:
                    cur = cur.left
                
                root.val = cur.val
                root.right = helper(root.right, cur.val)
            
            return root
        return helper(root, key)
            





            

            
        