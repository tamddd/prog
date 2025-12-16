module Main where

import Data.List
import Data.Function

main = do
    _ <- getLine
    s <- getLine
    let sorted_s = sort s
        counts = map (\g -> (head g, length g)) (group sorted_s)
        
        maxCount = maximum (map snd counts)
        
        ans = concat [ [char, '\n'] | (char, count) <- counts, count == maxCount ]
    
    putStrLn ans
