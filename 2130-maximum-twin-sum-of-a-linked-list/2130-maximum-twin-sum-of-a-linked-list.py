# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        # prerequisites
        # length ALWAYS even
        # min length in 2
        # twin sum =  node i + node n-1-i

        # 5 -> 2 -> 4 -> 1 -> 3 -> 2
        # 0    1    2    2 twin 1 twin 0 twin
        # node
        # twin
        # output return max twin sum
        # base case when len is 2

        # First I found middle node using fast slow pointers, slow will be middle node
        # I initialised a stack to hold twin values as top of stack will correspond to twin value for current node
        # I then populated this stack starting from middle node to end node ofo linked liist
        # Finally I started current node at head and calculated each twin sum by adding current node's value with top
        # of stack then popping that value from stack, comparing twinSum to max twinSum value and setting max accordingly

        # Time Complexity: O(n)
        # Space Complexity: O(n)

        if head.next.next == None:
            return head.val + head.next.val

        fast = slow = head
        # find middle
        while fast:
            slow = slow.next
            fast = fast.next.next

        # slow at start of twins
        twinVal = []
        cur = slow
        while cur:
            twinVal.append(cur.val)
            cur = cur.next

        # Checking max sum
        maxSum = 0
        cur = head
        while cur != slow:
            twinSum = cur.val + twinVal.pop()
            if twinSum > maxSum:
                maxSum = twinSum
            cur = cur.next
        return maxSum
            








        
                


           

           







        
            
            

        
         


        