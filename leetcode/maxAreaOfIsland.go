func maxAreaOfIsland(grid [][]int) int {
    height := len(grid)
    width := len(grid[0])
    var removeIsland func(y, x int) int
    removeIsland = func(y, x int) int {
        if grid[y][x] == 0 {
            return 0
        }
        grid[y][x] = 0
        cnt := 1
        var dy []int = []int{0, 1, 0, -1}
        var dx []int = []int{1, 0, -1, 0}
        for i := 0; i < 4; i++ {
            ny := y + dy[i]
            nx := x + dx[i]
            if 0 <= ny && ny < height && 0 <= nx && nx < width {
                cnt += removeIsland(ny, nx)
            }
        }
        return cnt
    }
    ans := 0
    for i := 0; i < height; i++ {
        for j := 0; j < width; j++ {
            if cnt := removeIsland(i, j); ans < cnt {
                ans = cnt
            }
        }
    }
    return ans
}
