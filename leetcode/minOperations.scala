import scala.collection.mutable.ArrayBuffer
object Solution {
  def minOperations(logs: Array[String]): Int = {
    var stack = ArrayBuffer.empty[String]
    for (log <- logs){
      if (log == "../"){
        if (stack.length != 0) stack.remove(stack.length - 1)
      } else if (log == "./") ()
      else {
        stack.append(log)
      }
    }
    stack.length
  }
}
