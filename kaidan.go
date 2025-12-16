/*package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scanf("%d", &n)
	dp := make([]int, n+1)
	dp[0] = 1
	dp[1] = 1

	for i := 2; i < n+1; i++ {
		dp[i] = dp[i-1] + dp[i-2]
	}

	fmt.Println(dp[n])
}
*/

package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scanf("%d", &n)

	dp := make([]int, n+1)
	dp[0] = 1
	for i := 1; i < n+1; i++ {
		if 0 <= i-1 {
			dp[i] += dp[i-1]
		}
		if 0 <= i-2 {
			dp[i] += dp[i-2]
		}
	}
	fmt.Println(dp[n])
}
