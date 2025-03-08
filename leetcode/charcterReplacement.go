func characterReplacement(s string, k int) int {
    var res int = 0
    for c := 'A'; c <= 'Z'; c++ {
        cnt := 0
        l := 0
        for r := 0; r < len(s); r++ {
            if s[r] == byte(c) {
                cnt++
            }

            for (r - l + 1) - cnt > k {
                if s[l] == byte(c) {
                    cnt--
                }
                l++
            }
            if res < r-l+1 {
                res = r-l+1
            }
        }    
    }
    return res
}
