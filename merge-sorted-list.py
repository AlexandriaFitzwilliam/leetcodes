# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 and not list2:
            return
        elif not list1 and list2:
            return list2
        elif list1 and not list2:
            return list1

        list1_mark = list1
        list2_mark = list2

        if list1_mark.val <= list2_mark.val:
            head_node = ListNode(val=list1.val)
            #change new position holder to list1.next
            list1_mark = list1_mark.next
        else:
            head_node = ListNode(val=list2.val)
            #change new position holder to list2.next
            list2_mark = list2_mark.next
        #change current node.next to be new_node
        #repeat until list.next=None

        cur = head_node
        print(f'head_node={head_node}')

        while list1_mark and list2_mark:
            print()
            print(f'list1_mark={list1_mark}')
            print(f'list2_mark={list2_mark}')
            print(f'cur={cur}')
            if list1_mark.val <= list2_mark.val:
                new_node = ListNode(val=list1_mark.val)
                list1_mark = list1_mark.next
            else:
                new_node = ListNode(val=list2_mark.val)
                list2_mark = list2_mark.next
            cur.next = new_node
            cur = new_node

        while list1_mark:
            print()
            print('inside while list1_mark')
            print(f'list1_mark={list1_mark}')
            print(f'cur={cur}')
            new_node = ListNode(val=list1_mark.val)
            list1_mark = list1_mark.next
            cur.next = new_node
            cur = new_node

        while list2_mark:
            print()
            print('inside while list2_mark')
            print(f'list2_mark={list2_mark}')
            print(f'cur={cur}')
            new_node = ListNode(val=list2_mark.val)
            list2_mark = list2_mark.next
            cur.next = new_node
            cur = new_node

        print(f'before return head_node={head_node}')
        return head_node