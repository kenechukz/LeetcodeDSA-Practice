# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        """
        342             243
        465             564
        807             708

        add two linked lists and store in same reversed order

        E:
        [1, 100]
        0 <= Node.val <= 9

        No leading 0s

        A:
        I could take values of each linked list
        make them num1 and num2, add the result then make 
        a linked list to store the result

        """


        num1 = num2 = 0

        i = 1

        cur = l1

        while cur != None:

            num1+= cur.val * i
            i *= 10
            cur = cur.next


        i = 1
        cur = l2
        while cur != None:

            num2+= cur.val * i
            i *= 10
            cur = cur.next
        
        res = str(num1 + num2)

        dummy = ListNode(-1)
        cur = dummy
        for digit in reversed(res):
            newNode = ListNode(int(digit))
            cur.next = newNode
            cur = newNode

        return dummy.next