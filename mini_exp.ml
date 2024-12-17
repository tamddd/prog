type operator = ADD | SUB
type func = FUNCTION
type expression =
  | Int of int
  | Expression of expression * operator * expression

let rec eval exp = match exp with
    Int exp -> exp
  | Expression (left, op, right) ->
     let left_exp = eval left in
     let right_exp = eval right in
     match op with
       ADD -> left_exp + right_exp
     | SUB -> left_exp - right_exp;;

let e1 = Expression (Int 1, ADD, Expression (Int 1, ADD, Int 100));;
print_int (eval e1)
