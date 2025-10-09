tails' :: [a] -> [[a]]
tails' [] = [[]]
tails' all@(x:xs) = [all] ++ tails' xs
