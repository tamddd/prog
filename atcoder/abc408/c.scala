object Main {
  def main(args: Array[String]): Unit = {
    val sc = new java.util.Scanner(System.in)
    val n = sc.nextInt()
    sc.nextLine()
    val ans = sc.nextLine().split("\\s+").map(_.toInt).toSet.toList.sorted
    println(ans.length)
    ans.map(println)
  }
}