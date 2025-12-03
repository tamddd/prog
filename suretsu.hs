#アルゴ式 数値の列

module Main where

solver 0 x y = x
solver 1 x y = y
solver n x y = (left + right) `mod` 100
    where 
        left = solver (n-1) x y
        right = solver (n-2) x y
main = do
    nxy <- getLine
    let [n, x, y] = map read $ words nxy :: [Int]
    putStrLn (show (solver (n-1) x y))
