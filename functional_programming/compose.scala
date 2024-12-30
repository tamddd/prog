def compose[A, B, C](f:B => C, g: A => B): A => C = {
    (a: A) => f(g(a))
}

val f = (x: Double) => math.Pi / 2 - x
val cos = f andThen math.sin