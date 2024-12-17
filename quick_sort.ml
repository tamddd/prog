let rec quick_sort lst = match lst with
    [] -> []
  | pivot :: rest ->
     let smaller_equal = List.filter (fun x -> x <= pivot) rest in
     let greater = List.filter (fun x -> pivot < x) rest in
     (quick_sort smaller_equal) @ [pivot] @ (quick_sort greater)
