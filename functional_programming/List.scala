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
        foldLeft(as, 0)((acc, _) => acc + 1)

    def sum3(is: List[Int]) = 
        foldLeft(is, 0)((acc, xs) => acc + xs)

    def reverse[A](as: List[A]) =
        foldLeft(as, Nil)((acc, x) => Cons(x, acc))

    def flatten[A](as: List[List[A]]) : List[A] = {
        //asはListのList appendはxにxsを追加する。
        foldLeft(as, Nil)((x, xs) => append(x, xs))
    }

    def addOneList(is: List[Int]) : List[Int] = {
        is match
            case Nil => Nil
            case Cons(head, tail) => Cons(head+1, addOneList(tail))
    }

    def myMap[A, B](as: List[A])(f: (A => B)) : List[B] = {
        as match
            case Nil => Nil
            case Cons(head, tail) => Cons(f(head), myMap(tail)(f))
    }

    def dtoStrList(ds: List[Double]) : List[String] =
        myMap(ds)(_.toString)

    def filter[A](as: List[A])(f: A => Boolean) : List[A] = {
        as match
            case Nil => Nil
            case Cons(head, tail) => if f(head) then Cons(head, filter(tail)(f)) else filter(tail)(f)
    }

    def filterEven(is: List[Int]) = 
        filter(is)((num) => num % 2 == 0)

    def flatMap[A, B](as: List[A])(f: A => List[B]) : List[B] = {
        as match
            case Nil => Nil
            case Cons(head, tail) => append(f(head), flatMap(tail)(f))
    }

    def addList(is1: List[Int], is2: List[Int]) : List[Int] = {
        (is1, is2) match
            case (Cons(h1, t1), Cons(h2, t2)) => Cons(h1+h2, addList(t1, t2))
            case _ => Nil
    }

    def zipWith[A, B](as1: List[A], as2: List[A])(f: (A, A) => B) : List[B] = {
        (as1, as2) match
            case (Cons(h1, t1), Cons(h2, t2)) => Cons(f(h1, h2), zipWith(t1, t2)(f))
            case _ => Nil
    }

    def main(args : Array[String]) : Unit = {
        println(flatMap(List(1, 2, 3))(i => List(i, i)))
    }
}