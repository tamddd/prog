let my_not pred =
  fun x -> not (pred x)

let even num =
  num mod 2 = 0

let odd num =
  my_not even num
