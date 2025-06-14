object Solution {
    def main(args: Array[String]) : Unit = {
        val n = scala.io.StdIn.readLine().toInt
        val a = scala.io.StdIn.readLine().split(" ").map(_.toInt)
        val k = scala.io.StdIn.readLine().toInt

        println(a.filter((x) => k <= x).length)
    }
}