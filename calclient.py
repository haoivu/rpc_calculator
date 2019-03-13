import rpyc
import sys
import builtins


def get_indices(arr, symbol):
    return [i for i, value in enumerate(arr) if value == symbol]


def parse_gen(arr):
    # Have to fix that */ and +- are same priority!!!!
    for symbol in ['**', '*', '/', '+', '-']:
        index_mover = 0

        #def print(*args):
         #   if symbol == '+':
          #      builtins.print(*args)

        for index in get_indices(arr, symbol):
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
            print('After ', symbol)
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
conn = rpyc.connect("localhost", 12345)
#x = conn.root.checker(args)
x = parse_gen(args)
print(x)
exit()

try:
    y = conn.root.div(4,0)
    print(y)
except ZeroDivisionError:
    print("ZeroDivisionError")
    pass
conn.close()
