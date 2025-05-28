package main

import (
	"fmt"
)

func main() {
	var s string
	fmt.Scanf("%s", &s)
	var ans int = int(s[len(s)-1]) - int('0')

	for i := len(s) - 2; i >= 0; i-- {
		v := int(s[i]) - int('0')
		u := int(s[i+1]) - int('0')
		b := (10 + v - u) % 10
		if b < 0 {
			b = -b
		}
		ans += b
	}
	fmt.Println(ans + len(s))
}
