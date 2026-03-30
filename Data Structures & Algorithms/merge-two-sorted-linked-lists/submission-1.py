# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = dummy = ListNode()

        while list1 and list2:
            print('head.val: ', dummy.val)
            print('list1.val:', list1.val, 'list2.val:', list2.val)
            if list1.val <= list2.val:
                print('Added list1.val')
                dummy.next = list1
                list1 = list1.next
            else:
                print('Added list2.val')
                dummy.next = list2
                list2 = list2.next
            print('\n')
            
            dummy = dummy.next

        if list1:
            print('Added rest of list1 because list2 is null now')
            dummy.next = list1
        if list2:
            print('Added rest of list2 because list1 is null now')
            dummy.next = list2

        return head.next