func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	dummyHead := &ListNode{Next: nil}
	res := dummyHead
	for list1 != nil && list2 != nil {
		if list1.Val <= list2.Val {
			dummyHead.Next = list1
			list1 = list1.Next
		} else {
			dummyHead.Next = list2
			list2 = list2.Next
		}
		dummyHead = dummyHead.Next
	}

	if list1 != nil {
		dummyHead.Next = list1
	}
	if list2 != nil {
		dummyHead.Next = list2
	}

	return res.Next
}
