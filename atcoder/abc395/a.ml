let n = read_int ()

let xs = read_line ()
  |> String.split_on_char ' '
  |> List.map int_of_string

let rec solver lst prev = match lst with
    [] -> true
  | first :: rest ->
     if prev < first then solver rest first
     else false

let ans = solver xs (-1)
let () =
  print_endline (if ans then "Yes" else "No")
