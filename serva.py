import rpyc
from rpyc.utils.server import ThreadedServer  # or ForkingServer


def sub(a, b):
    return float(a) - float(b)


def add(a, b):
    return float(a) + float(b)


class Delegator(rpyc.Service):
    def exposed_checker(self, args):
        print(args)

        if '+' in args:
            return add(args[0], args[2])
        elif '-' in args:
            return sub(args[0], args[2])
        elif '/' in args:
            print('fjslka1')
            conn = rpyc.connect("localhost", 12346)
            x = conn.root.div(args[0], args[2])
            conn.close()
            return x
        elif '*' in args:
            conn = rpyc.connect("localhost", 12346)
            x = conn.root.mul(args[0], args[2])
            conn.close()
            return x
        elif '**' in args:
            conn = rpyc.connect("localhost", 12347)
            x = conn.root.power(args[0], args[2])
            conn.close()
            return x


if __name__ == "__main__":
    server = ThreadedServer(Delegator, port=12345)
    print('Start delegate server')
    server.start()
    print('Stop server')
