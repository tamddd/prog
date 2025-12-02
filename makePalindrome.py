n = int(input())
x = input()

def make_palindrome(l, idx):
    if idx == n:
        return l
    else:
        c = x[idx]
        l = l + [c] + l[::-1]
        palm = make_palindrome(l, idx+1)
        return palm

res = make_palindrome([], 0)
print("".join(res))
