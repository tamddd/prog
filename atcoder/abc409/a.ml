let _ = read_int () in
    let t = read_line () in
    let a = read_line () in
    let rec solver a b n =
      if String.length a == n then true
      else
        let na = String.get a n in
        let nb = String.get b n in
        if na == 'o' &&  na == nb then false
        else solver a b (n+1) in 
    let ans = if not (solver t a 0) then "Yes" else "No" in 
    print_endline ans;;
