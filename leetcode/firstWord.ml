let firstWord s =
  let words = String.split_on_char ' ' s in
  let filtered_words = List.filter (fun x -> String.length x > 0) words in
  match filtered_words with
    [] -> ""
  | first :: rest -> first
