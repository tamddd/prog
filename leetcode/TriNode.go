package TriNode

type TriNode struct {
	children    map[rune]*TriNode
	isEndOfWord bool
}

func newTriNode() *TriNode {
	return &TriNode{children: make(map[rune]*TriNode), isEndOfWord: false}
}

type PrefixTree struct {
	root *TriNode
}

func Constructor() *PrefixTree {
	return &PrefixTree{root: newTriNode()}
}

func (this *PrefixTree) Insert(word string) {
	cur := this.root
	for _, c := range word {
		if _, ok := cur.children[c]; !ok {
			cur.children[c] = newTriNode()
		}
		cur = cur.children[c]
	}
	cur.isEndOfWord = true
}

func (this *PrefixTree) Search(word string) bool {
	cur := this.root
	for _, c := range word {
		if _, ok := cur.children[c]; !ok {
			return false
		}
		cur = cur.children[c]
	}
	return cur.isEndOfWord
}

func (this *PrefixTree) StartsWith(prefix string) bool {
	cur := this.root

	for _, c := range prefix {
		if _, ok := cur.children[c]; !ok {
			return false
		}
		cur = cur.children[c]
	}
	return true
}
