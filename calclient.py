import rpyc
import sys

print(sys.argv)


conn = rpyc.connect("localhost", 12345)
x = conn.root.checker(sys.argv[1:])
# assert x == 11
print(x)
exit()

try:
    y = conn.root.div(4,0)
    print(y)
except ZeroDivisionError:
    print("ZeroDivisionError")
    pass
conn.close()
