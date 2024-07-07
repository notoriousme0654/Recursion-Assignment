def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
l1 = ListNode(1, ListNode(3, ListNode(5)))
l2 = ListNode(2, ListNode(4, ListNode(6)))
print("List 1:")
print_linked_list(l1)
print("List 2:")
print_linked_list(l2)
merged_head = merge_two_lists(l1, l2)
print("Merged Linked List:")
print_linked_list(merged_head)
