applyTwice :: (a -> a) -> a -> a
applyTwice f val = f (f val)
