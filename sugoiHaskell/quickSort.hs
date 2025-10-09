quickSort :: (Ord a) => [a] -> [a]
quickSort [] = []
quickSort (x:xs) =
  let smallerEqual = [a | a <- xs, a <= x]
      larger = [a | a <- xs, x < a] in 
    quickSort smallerEqual ++ [x] ++ quickSort larger


isSorted :: (Ord a) => [a] -> Bool
isSorted [] = True
isSorted [x] = True
isSorted (x:y:xs)
  | x <= y = isSorted (y:xs)
  | otherwise = False
