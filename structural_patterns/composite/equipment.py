from abc import ABCMeta, abstractmethod


class Equipment(metaclass=ABCMeta):

    def __init__(self, net_price):
        assert isinstance(net_price, int)
        self._net_price = net_price

    def get_net_price(self):
        return self._net_price

    def add(self, equipment):
        raise ReferenceError('Not a composite class')

    def remove(self, equipment):
        raise ReferenceError('Not a composite class')

    @abstractmethod
    def get_name(self):
        raise NotImplementedError()