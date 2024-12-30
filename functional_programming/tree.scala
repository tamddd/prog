sealed trait Tree[+A]
case class Leaf[A](value: A) extends Tree[A]
case class Branch[A](left: Tree[A], right: Tree[A]) extends Tree[A]

object Tree {
    def size[A](at: Tree[A]) : Int = {
        at match
            case Branch(left, right) => size(left) + size(right)
            case _ => 1
    }

    def maximum(it: Tree[Int]) : Int = {
        it match
            case Branch(left, right) => maximum(left).max(maximum(right))
            case Leaf(x) => x
    }

    def map[A, B](at: Tree[A])(f: (A => B)) : Tree[B] = {
        at match
            case Leaf(x) => Leaf(f(x))
            case Branch(left, right) => Branch(map(left)(f), map(right)(f))
        
    }


    def main(args : Array[String]) : Unit = {
        val f = Branch(Branch(Leaf(123), Leaf(32)),
        Branch(Leaf(-12), Leaf(2)))
        println(maximum(map(f)(x => x * 123)))
    }
}