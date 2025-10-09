size :: [a] -> Int
size [] = 0
size [_] = 1
size (x:xs) = 1 + size xs
