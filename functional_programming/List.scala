sealed trait List[+A]
case object Nil extends List[Nothing]
case class Cons[+A](head: A, tail: List[A]) extends List[A]

object List {
    def sum(ints: List[Int]) : Int = ints match {
        case Nil => 0
        case Cons(x, xs) => x + sum(xs)
    }

    def product(ds: List[Double]): Double = ds match {
        case Nil => 1.0
        case Cons(0.0, _) => 0.0
        case Cons(x, xs) => x * product(xs)
    }

    def apply[A](as: A*): List[A] = {
        if (as.isEmpty) Nil
        else Cons(as.head, apply(as.tail: _*))
    }

    def tail[A](as: List[A]): List[A] = {
        as match {
            case Cons(head, next) => next
            case _ => Nil
        }
    }

    def setHead[A](as: List[A], head: A) : List[A] = {
        as match {
            case Cons(_, tail) => Cons(head, tail)
            case _ => Cons(head, Nil)
        }
    }

    def drop[A](as: List[A], dropCount: Int) : List[A] = {
        if (dropCount < 0) as 
        else {
            as match
                case Nil => Nil
                case Cons(_, tail) => drop(tail, dropCount -1)
        }
    }

    def dropWhile[A](l: List[A], f: A => Boolean) : List[A] = {
        l match {
            case Nil => Nil
            case Cons(head, tail) if (f(head)) => dropWhile(tail, f)
            case _ => l
        }
    }

    //a1が尽きるまで値をコピーする　
    def append[A](a1: List[A], a2: List[A]) : List[A] = {
        a1 match {
            case Nil => a2
            case Cons(head, tail) => Cons(head, append(tail, a2))
        }
    }

    def foldRight[A, B](as: List[A], z:B)(f: (A, B) => B) : B = {
        as match
            case Nil => z
            case Cons(head, tail) => f(head, foldRight(tail, z)(f))
        
    }

    def length[A](as: List[A]) =
        foldRight(as, 0)((_, xs) => 1 + xs)

    def sum2(ns: List[Int]) = 
        foldRight(ns, 0)((x, y) => x + y)

    def foldLeft[A, B](as: List[A], z: B)(f: (B, A) => B) : B = {
        as match {
            case Nil => z
            case Cons(head, tail) => foldLeft(tail, f(z, head))(f)
        }
    }

    def length2[A](as: List[A]) = 
        foldLeft(as, 0)((acc, _) => 1 + acc)

    def reverse[A](as: List[A]) =
        foldLeft(as, Nil)((acc, x) => Cons(x, acc))

    def flatten[A](as: List[List[A]]) : List[A] = {
        foldLeft(as, Nil)((x, xs) => append(x, xs))
    }

    def main(args : Array[String]) : Unit = {
        val x = List(1, 2, 3, 4, 5) match {
        case Cons(x, Cons(2, Cons(4, _))) => x
        case Nil => 42
        //ここに引っかかる
        case Cons(x, Cons(y, Cons(3, Cons(4, _)))) => x + y
        case Cons(h, t) => h + sum(t)
        case _ => 101
        }
        println(x)
    }
}