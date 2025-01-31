import sys

operators = {"+", "-", "*", "/"}

i = 0
def skip_space():
    global i, expression
    while i < len(expression) and expression[i] == " ":
        i += 1

def eval():
    global i, expression
    skip_space()

    if i >= len(expression):
        return
    
    if expression[i].isdigit():
        val = int(expression[i])
        i += 1
        while i < len(expression) and expression[i].isdigit():
            val *= 10
            val += int(expression[i])
            i += 1
        return val
    else:
        if expression[i] in operators:
            ope = expression[i]
            i += 1
            left = eval()
            right = eval()
            print(left, right, ope)
            if ope == "+":
                return left + right
            elif ope == "-":
                return left - right
            elif ope == "*":
                return left * right
            elif ope == "/":
                return left / right

if __name__ == "__main__":
    expression = " ".join(sys.argv[1:])
    print(eval())
