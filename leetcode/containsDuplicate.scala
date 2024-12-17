object Solution {
  def containsDuplicate(nums: Array[Int]): Boolean = {
    val sortedNums = nums.sorted
    def solver(prev: Int, nums: Array[Int]) : Boolean = {
      if (nums.length == 0) false
      else {
        if (prev == nums.head) true
        else solver(nums.head, nums.tail)
      }
    }
    solver(sortedNums.head, sortedNums.tail)
  }
}
