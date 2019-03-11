import rpyc
from rpyc.utils.server import ThreadedServer  # or ForkingServer


class CalculatorService(rpyc.Service):
    def exposed_mul(self, a, b):
        return float(a) * float(b)

    def exposed_div(self, a, b):
        return float(a) / float(b)

    def foo(self):
        print("foo")


if __name__ == "__main__":
    server = ThreadedServer(CalculatorService, port=12346)
    print('Start muldiv server')
    server.start()
    print('Stop server')
