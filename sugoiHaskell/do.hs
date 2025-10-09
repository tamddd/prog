main = do
  putStrLn "input number"
  input <- getLine
  let num = read input :: Int
  print(num * 121)


