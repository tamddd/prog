import sys

operators = {"+", "-", "*", "/"}

def skip_space():
    global i, expression
    while i < len(expression) and expression[i] == " ":
        i += 1

def register_func(c, func_name):
    global i, expression
    i += 2
    l = []
    while i < len(expression) and expression[i] != c:
        l.append(expression[i])
        i += 1
    function_table[func_name] = "".join(l)
    return

def eval_string(func_name, args):
    global i, expression
    fn = function_table[func_name]
    l = []
    for c in fn:
        if "a" <= c <= "z":
          l.append(args.pop())
        else:
            l.append(c)
    ci = i
    code = expression
    i = 0
    expression = "".join(l)
    val = eval()
    i = ci
    expression = code
    return val

def eval():
    global i, expression

    skip_space()
    if i >= len(expression):
        return

    #関数定義
    if "A" <= expression[i] <= "Z"\
    and i + 1 < len(expression) and expression[i+1] == "[":
        register_func("]", expression[i])
        i += 1
        return eval()
    #関数呼び出し
    if "A" <= expression[i] <= "Z"\
    and i + 1 < len(expression) and expression[i+1] == "(":
        func_name = expression[i]
        args = []
        i += 2
        while i < len(expression) and expression[i] != ")":
            skip_space()
            args.append(str(eval()))
            skip_space()
        val = eval_string(func_name, args[::-1])
        i += 1
        return val

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
            if ope == "+":
                return left + right
            elif ope == "-":
                return left - right
            elif ope == "*":
                return left * right
            elif ope == "/":
                return left // right

if __name__ == "__main__":
    #関数は一文字
    function_table = {}
    i = 0
    expression = "+ 1 1"
    assert 2 == eval()
    
    i = 0
    expression = "* 1 1"
    assert 1 == eval()

    i = 0
    expression = "* + 10 10 10"
    assert 200 == eval()

    i = 0
    function_table = {}
    expression = "A[* a b] A(2A(A(A(A(2 2) 2) 2) 2))"
    assert 64 == eval()
