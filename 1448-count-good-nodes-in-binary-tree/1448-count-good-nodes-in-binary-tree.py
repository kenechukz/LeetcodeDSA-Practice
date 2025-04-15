# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # Check if root is empty
        if root:
            numGoodNodes = 1
        else:
            return 0
        nodes = []
        def recursion(root, numGoodNodes, nodes)  -> int:

            if root == None:
                return 0

            

            
            # compare current root val to greatest of previous nodes
            if nodes:
                if root.val >= nodes[-1]:
                    numGoodNodes += 1
            


                
            nodes.append(root.val)
            # so biggest value at last index
            nodes.sort()
            
            
            
            numGoodNodes += recursion(root.left,0,nodes) + recursion(root.right,0,nodes)
            # remove node after recursive call from array
            nodes.remove(root.val)

            return numGoodNodes

            


        return recursion(root, numGoodNodes, nodes)

            



        
        