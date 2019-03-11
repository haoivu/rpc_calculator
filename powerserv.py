import rpyc
from rpyc.utils.server import ThreadedServer  # or ForkingServer


class CalculatorService(rpyc.Service):
    def exposed_power(self, a, b):
        return float(a) ** float(b)


if __name__ == "__main__":
    server = ThreadedServer(CalculatorService, port=12347)
    print('Start power server')
    server.start()
    print('Stop server')
