type tree =
  Leaf
| Branch of tree * int * tree

let rec treeSum tree = match tree with
    Leaf -> 0
  | Branch (left, v, right) ->
     (treeSum left) + v + (treeSum right)

let rec treeMap tree func = match tree with
    Leaf -> Leaf
  | Branch (left, v, right) ->
     Branch(treeMap left func, func v, treeMap right func)
