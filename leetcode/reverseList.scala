object Solution {
    def reverseList(head: ListNode): ListNode = {
        solver(null, head)
    }

    def solver(pre: ListNode, cur: ListNode) : ListNode = {
        if (cur == null) {
            pre
        }
        else {
            val cur_next = cur.next
            cur.next = pre
            solver(cur, cur_next)
        }
    }
}