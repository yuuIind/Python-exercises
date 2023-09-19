# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode()
        digit = result
        carry = 0
        while (l1 != None) or (l2 != None) or carry != 0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            digitSum = carry + val1 + val2
            digit.next = ListNode(val=(digitSum % 10))
            carry = digitSum // 10
            digit = digit.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return result.next      