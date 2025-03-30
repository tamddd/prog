/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type nodeInterface struct {
    count int
    node *TreeNode
}

func minDepth(root *TreeNode) int {
	if root == nil {
		return 0;
	}
    deque := list.New()
    deque.PushBack(nodeInterface{count:1, node:root})
    var ans int = math.MaxInt32
    for deque.Len() > 0 {
        element := deque.Front()
        nodeInfo := element.Value.(nodeInterface)
        deque.Remove(element)
        node := nodeInfo.node
        count := nodeInfo.count
        if node.Left == nil && node.Right == nil {
            if count < ans {
                ans = count
            }
        }
        if node.Left != nil {
            deque.PushBack(nodeInterface{count:count+1, node:node.Left})
        }

        if node.Right != nil {
            deque.PushBack(nodeInterface{count:count+1, node:node.Right})
        }
    }
    return ans
}
