n = int(input())

def is_fizz(n):
    if n % 3 == 0 and n % 5 != 0:
        return True
    else:
        return False

print(len([i for i in range(1, n) if is_fizz(i)]))
