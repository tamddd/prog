ps = input()

if all([i.isdigit() for i in ps]) and len(ps) == 4:
    print("valid")
else:
    print('invalid')
