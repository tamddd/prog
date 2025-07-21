import scala.math.BigInt

object MathTest extends App {
  def factorial(n: Int): BigInt = {
    if (n == 0) 1 else n * factorial(n - 1)
  }
  println(factorial(10))


  def gcd(a: Int, b: Int): Int = {
    if (a == 0) b
    else if (b == 0) a
    else gcd(b, a % b)
  }
}