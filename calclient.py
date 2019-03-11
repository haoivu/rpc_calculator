import rpyc
import sys


def get_indices(arr, symbol):
    indices = []
    for i, value in enumerate(arr):
        if value == symbol:
            indices.append(i)
    return indices


def parse_gen(arr):

    index_mover = 0
    for index in get_indices(arr, '**'):
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
        index_mover -= 2

    index_mover = 0
    for index in get_indices(arr, '*'):
        conn = rpyc.connect("localhost", 12345)
        x = conn.root.checker(arr[index - 1 - index_mover:index + 2 - index_mover])
        front = arr[:index - 1 - index_mover]
        if (index + 2 - index_mover) == len(arr):
            # End of array
            back = []
        else:
            back = arr[index + 2 - index_mover:]
        simplified = front + [x] + back
        arr = simplified
        index_mover -= 2

    index_mover = 0
    for index in get_indices(arr, '/'):
        conn = rpyc.connect("localhost", 12345)
        x = conn.root.checker(arr[index - 1 - index_mover:index + 2 - index_mover])
        front = arr[:index - 1 - index_mover]
        if (index + 2 - index_mover) == len(arr):
            # End of array
            back = []
        else:
            back = arr[index + 2 - index_mover:]
        simplified = front + [x] + back
        arr = simplified
        index_mover -= 2

    index_mover = 0
    for index in get_indices(arr, '+'):
        conn = rpyc.connect("localhost", 12345)
        x = conn.root.checker(arr[index - 1 - index_mover:index + 2 - index_mover])
        front = arr[:index - 1 - index_mover]
        if (index + 2 - index_mover) == len(arr):
            # End of array
            back = []
        else:
            back = arr[index + 2 - index_mover:]
        simplified = front + [x] + back
        arr = simplified
        index_mover -= 2

    index_mover = 0
    for index in get_indices(arr, '-'):
        conn = rpyc.connect("localhost", 12345)
        x = conn.root.checker(arr[index - 1 - index_mover:index + 2 - index_mover])
        front = arr[:index - 1 - index_mover]
        if (index + 2 - index_mover) == len(arr):
            # End of array
            back = []
        else:
            back = arr[index + 2 - index_mover:]
        simplified = front + [x] + back
        arr = simplified
        index_mover -= 2

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
