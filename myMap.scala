def map[T, U](list: List[T])(f: T=>U): List[U] =
  list.foldLeft(Nil: List[U]){(x, y) => f(y) :: x}.reverse
