/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func getDecimalValue(head *ListNode) int {
    res := 0
    tmp := head

    for tmp != nil {
        res *= 2
        res += tmp.Val
        tmp = tmp.Next
    }

    return res
}
