object Module {
  def abs(x: Int) : Int = {
    if (x < 0) -x
    else x
  }
  def formatAbs(x : Int) = {
    val msg = "The abs value of %d is %d"
    msg.format(x, abs(x))
}
}
