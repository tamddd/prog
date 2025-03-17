let n = read_int ()

let rec get_words n =
  if n = 0 then []
  else [read_line ()] @ get_words (n-1)

let rec quick_sort lst = match lst with
    [] -> []
  | pivot :: rest ->
     let smaller = List.filter (fun x -> String.length x < String.length pivot) rest in
     let greater_equal = List.filter (fun x -> String.length pivot <= String.length x) rest in
     (quick_sort smaller) @ [pivot] @ (quick_sort greater_equal)

let rec print_words l = match l with
    [] -> print_endline ""
  | first :: rest ->
     begin
       print_string first;
       print_words rest
     end

let () =
  print_words (quick_sort (get_words n))
