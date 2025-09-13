import scala.io.StdIn.readLine

object Main extends App {    
    val Array(x, y) = readLine().split(" ").map(_.toLong)  
    println(solver(10))
    def solver(n: Long): Long = {
        if (n==1) x
        else if (n==2) y
        else {
            (solver(n-1) + solver(n-2)).toString.reverse.toLong
        }
    }
}
