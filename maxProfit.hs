#アルゴ式 最大瞬間利益
module Main where

main = do
    l <- getLine
    t <- getLine
    let wt = map read $ words t :: [Int]
        ans = maximum $ scanl1 (+) wt
    putStrLn (show ans)
