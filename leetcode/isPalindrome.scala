object Solution {
  def getNextIndex(s: String, idx: Int, flg: Boolean): Int = {
    if (idx < 0 || idx >= s.length) return -1
    if (s.charAt(idx).isLetterOrDigit) return idx
    getNextIndex(s, idx + (if (flg) -1 else 1), flg)
  }

  def isPalindrome(s: String): Boolean = {
    var left = 0
    var right = s.length - 1

    while (left <= right) {
      left = getNextIndex(s, left, false)
      right = getNextIndex(s, right, true)

      if (left == -1 || right == -1) return true

      if (s.charAt(left).toLower != s.charAt(right).toLower) return false

      left += 1
      right -= 1
    }
    true
  }
}
