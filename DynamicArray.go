package DynamicArray

type DynamicArray struct {
	cap int
	arr []int
	idx int
}

func NewDynamicArray(capacity int) *DynamicArray {
	return &DynamicArray{cap: capacity, arr: make([]int, 0, capacity), idx: 0}
}

func (da *DynamicArray) Get(i int) int {
	return da.arr[i]
}

func (da *DynamicArray) Set(i int, n int) {
	da.arr[i] = n
}

func (da *DynamicArray) Pushback(n int) {
	da.arr = append(da.arr, n)
	da.idx++
}

func (da *DynamicArray) Popback() int {
	tmp := da.idx - 1
	da.idx -= 1
	return da.arr[tmp]
}

func (da *DynamicArray) resize() {
	da.arr = append(da.arr, -1)
}

func (da *DynamicArray) GetSize() int {
	return da.idx
}

func (da *DynamicArray) GetCapacity() int {
	return cap(da.arr)
}
