sealed trait Tree[+A]
case class Leaf[A](value: A) extends Tree[A]
case class Branch[A](left: Tree[A], right: Tree[A]) extends Tree[A]

object Tree {
    def size[A](at: Tree[A]) : Int = {
        at match
            case Branch(left, right) => size(left) + size(right)
            case _ => 1
    }


    def main(args : Array[String]) : Unit = {
        val f = Branch(Branch(Leaf("a"), Leaf("B")),
        Branch(Leaf("c"), Leaf("d")))
        println(size(f))
    }
}