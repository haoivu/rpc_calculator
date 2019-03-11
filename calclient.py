import rpyc

conn = rpyc.connect("localhost", 12345)
x = conn.root.add(4, 7)
assert x == 11
print(x)

try:
    y = conn.root.div(4,0)
    print(y)
except ZeroDivisionError:
    print("ZeroDivisionError")
    pass
conn.close()
