let () =
  let x = read_float () in
  let ans = match x with
    | n when n >= 38.0 -> "1"
    | n when n >= 37.5 -> "2"
    | _ -> "3"
  in
  print_endline ans
  ;;
