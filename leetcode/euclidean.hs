module Main where

solver x 0 = x
solver x y = solver y (x `mod` y)

main = do
    nm <- getLine
    let [n, m] = map read $ words nm :: [Int]
    putStrLn (show $ solver n m)
