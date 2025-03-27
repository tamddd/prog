let rec solver l r s =
(*  print_int l;
  print_endline "";
  print_int r;
  print_endline "";*)
  if l >= r then s.[l] == '/'
  else
    if s.[l] == '1' && s.[r] == '2' then
      solver (l+1) (r-1) s
    else false;;

() =
  let n = read_int () in
  let s = read_line () in
  print_endline (if solver 0 (n-1) s then "Yes" else "No")
