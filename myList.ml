type myList = Empty | Node of int * myList

let rec myListMap lst f = match lst with
    Empty -> Empty
  | Node (v, rest) -> Node (f v, myListMap rest f);;

let rec myListPrint lst = match lst with
    Empty -> print_endline ""
  | Node (v, rest) ->
     begin
       print_int v;
       print_endline " ";
       end;;

() = myListPrint (myListMap(Node (1, Empty)) (fun x -> x * 10))
