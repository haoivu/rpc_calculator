import rpyc
import sys
import builtins


def get_indices(arr, symbols):
    return [i for i, value in enumerate(arr) if value in symbols]


def parse_gen(arr):
    for symbols in [['**'], ['*', '/'], ['+', '-']]:
        index_mover = 0

        #def print(*args):
         #   if symbol == '+':
          #      builtins.print(*args)

        for index in get_indices(arr, symbols):
            conn = rpyc.connect("localhost", 12345)
            x = conn.root.checker(arr[index-1-index_mover:index+2-index_mover])
            front = arr[:index-1-index_mover]
            if (index+2-index_mover) == len(arr):
                # End of array
                back = []
            else:
                back = arr[index+2-index_mover:]
            simplified = front + [x] + back
            arr = simplified
            index_mover += 2
            print('After ', symbols)
            print(arr, '\n')

    assert len(arr) == 1, arr
    return arr[0]


def parenth(arr):
    lparen = []
    rparen = []
    for i, value in enumerate(arr):
        if value == '(':
            lparen.append(i)
        elif value == ')':
            rparen.append(i)

        print(i, value)
    assert len(lparen) == len(rparen), 'Error: parenthesis mismatch'

    for i in range(len(rparen)-1, -1, -1):
        pass


def listRightIndex(alist, value):
    return len(alist) - alist[-1::-1].index(value) - 1


def parenth2(arr):
    if '(' in arr:
        assert arr.count('(') == arr.count(')'), 'Error: parenthesis mismatch'
        rpar = arr.index(')') + 1
        lpar = listRightIndex(arr[:rpar], '(')

        print(arr[lpar:rpar])
        #print(lpar)
        #print(rpar)
        #print(arr)
        arr = arr[:lpar] + [parse_gen(arr[lpar+1:rpar-1])] + arr[rpar:]
        print(arr)
        return parenth2(arr)
    else:
        return parse_gen(arr)

print(sys.argv)

args = []
if len(sys.argv) == 1:
    print('Please enter arguments')
    exit()
elif len(sys.argv) == 2:
    args = sys.argv[1].strip().split()
else:
    args = sys.argv[1:]

print(args)
try:
    x = parenth2(args)
    print(x)
except ZeroDivisionError:
    print("ZeroDivisionError")
    pass
