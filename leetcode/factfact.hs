module Main where

solver n
  | n >= 3 = n * (solver (n-2))
  | otherwise = n

main = do
  sn <- getLine
  let n = read sn :: Int
  putStrLn (show $ solver n)
