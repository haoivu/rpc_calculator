import rpyc
from rpyc.utils.server import ThreadedServer  # or ForkingServer


class MyService(rpyc.Service):
    #
    # ... you service's implementation
    print("myservices class")
    #
    pass


class CalculatorService(rpyc.Service):
    def exposed_add(self, a, b):
        return a + b

    def exposed_sub(self, a, b):
        return a - b

    def exposed_mul(self, a, b):
        return a * b

    def exposed_div(self, a, b):
        return a / b

    def foo(self):
        print("foo")


class Delegator(rpyc.Service):
    def exposed_add(self, a, b):
        return a + b

    def exposed_sub(self, a, b):
        return a - b

    def checker(self, input=''):
        print(input)
        if input.split()[-1] == '/':
            conn = rpyc.connect("localhost", 12346)
            x = conn.root.add(4, 7)


if __name__ == "__main__":
    server = ThreadedServer(Delegator, port=12345)
    # server = ThreadedServer(CalculatorService, port=12345)
    server.start()
    print("server start()")
