n = int(input())
def fib(n):
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)
list(map(lambda x : print(x), list(map(lambda x : fib(x), range(1, n+1)))))
