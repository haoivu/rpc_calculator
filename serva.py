import rpyc
from rpyc.utils.server import ThreadedServer  # or ForkingServer


class Delegator(rpyc.Service):
    def add(self, a, b):
        return float(a) + float(b)

    def sub(self, a, b):
        return float(a) - float(b)

    def exposed_checker(self, args):
        print(args)

        if '+' in args:
            return self.add(args[0], args[1])
        elif '-' in args:
            return self.sub(args[0], args[1])
        elif '/' in args:
            print('fjslka1')
            conn = rpyc.connect("localhost", 12346)
            x = conn.root.div(args[0], args[1])
            conn.close()
            return x
        elif '*' in args:
            conn = rpyc.connect("localhost", 12346)
            x = conn.root.mul(args[0], args[1])
            conn.close()
            return x
        elif '**' in args:
            conn = rpyc.connect("localhost", 12347)
            x = conn.root.power(args[0], args[1])
            conn.close()
            return x


if __name__ == "__main__":
    server = ThreadedServer(Delegator, port=12345)
    print('Start delegate server')
    server.start()
    print('Stop server')
