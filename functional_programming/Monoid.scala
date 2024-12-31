trait Monoid[A] {
    def op(a1: A, a2: A): A
    def zero: A
}

val stringMonoid = new Monoid[String] {
    def op(a1: String, a2: String): String = a1+a2
    val zero = ""
}

val intMonoid = new Monoid[Int] {
    def op(a1: Int, a2: Int): Int = a1 + a2
    val zero = 0
}

val words = List("Heloo!!!", "WORLD!!!")
val s = words.foldLeft(stringMonoid.zero)(stringMonoid.op)

def concatenate[A](as: List[A], m: Monoid[A]): A = {
    as.foldLeft(m.zero)(m.op)
}

def foldMap[A,B](as: List[A], m: Monoid[B])(f: A => B) : B = {
    as.foldLeft(m.zero)((b, a) => m.op(b, f(a)))
}

def foldMapV[A, B](v: IndexedSeq[A], m: Monoid[B])(f: A => B) : B = {
    if (v.length == 0) then m.zero
    else if (v.length == 1) then f(v(0))
    else 
        val (l, r) = v.splitAt(v.length / 2)
        //foldMapVで返ってくるのはBだから、opで結合できる
        m.op(foldMapV(l, m)(f), foldMapV(r, m)(f))
}