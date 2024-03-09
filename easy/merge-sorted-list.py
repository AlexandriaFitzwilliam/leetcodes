# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        #checks if both lists are empty
        if not list1 and not list2:
            return
        #checks if just one list is empty, if so returns the other head node
        elif not list1 and list2:
            return list2
        elif list1 and not list2:
            return list1

        #markers to keep track where current location in node chain we're at
        list1_mark = list1
        list2_mark = list2


        #sets first head node for our new merged list
        if list1_mark.val <= list2_mark.val:
            head_node = ListNode(val=list1.val)
            list1_mark = list1_mark.next
        else:
            head_node = ListNode(val=list2.val)
            list2_mark = list2_mark.next


        #keep track of where we are in our merged list
        cur = head_node

        #loop through and checks if there are still nodes to look at
        while list1_mark and list2_mark:
            if list1_mark.val <= list2_mark.val:
                new_node = ListNode(val=list1_mark.val)
                list1_mark = list1_mark.next
            else:
                new_node = ListNode(val=list2_mark.val)
                list2_mark = list2_mark.next
            #now we know where the next pointer should go, so we assign it
            cur.next = new_node
            #moves our current location to end of current list
            cur = new_node

        #at this point, one of the given list has no more markers
        #so loops through both list (if they exist) to add the rest of the nodes to our new merged list
        while list1_mark:
            new_node = ListNode(val=list1_mark.val)
            list1_mark = list1_mark.next
            cur.next = new_node
            cur = new_node

        while list2_mark:
            new_node = ListNode(val=list2_mark.val)
            list2_mark = list2_mark.next
            cur.next = new_node
            cur = new_node

        return head_node