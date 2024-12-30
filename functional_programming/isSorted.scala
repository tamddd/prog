def isSorted[A](as: Array[A], order:(A, A) => Boolean) : Boolean = {
    def loop(n: Int): Boolean = {
        if (n >= as.length) true
        else if (order(as(n), as(n+1))) loop(n+1)
        else false
    }
    loop(0)
}

//無名関数の書き方
val f = (x: Int) => x + 123