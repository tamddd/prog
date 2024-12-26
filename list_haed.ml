let rec reverseList lst = match lst with
    [] -> []
  | first :: rest ->
     (reverseList rest) @ [first];;

let listHead lst = match lst with
    [] -> []
  | first :: rest -> first;;


let last lst = listHead(reverseList lst)
