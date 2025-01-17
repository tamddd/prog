package main

type Node struct {
	val  int
	next *Node
}

type List struct {
	head *Node
}

func (l *List) add(val int) {
	if l == nil {
		l.head = &Node{val: val}
	} else {
		tmp := l.head
		for tmp.next != nil {
			tmp = tmp.next
		}
		tmp.next = &Node{val: val}
	}
}

func (l *List) print() {
	tmp := l.head

	for tmp != nil {
		println(tmp.val)
		tmp = tmp.next
	}
}

func main() {
	l := &List{head: &Node{val: 10, next: nil}}
	l.print()
}
