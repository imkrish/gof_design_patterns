from structural_patterns.composite.equipment import Equipment
from abc import abstractmethod, ABCMeta


class CompositeEquipment(Equipment, metaclass=ABCMeta):

    def __init__(self, net_price):
        super().__init__(net_price)
        self.__children = []

    def get_net_price(self):
        net_price = self._net_price
        for child in self.__children:
            net_price += child.get_net_price()
        return net_price

    def add(self, equipment):
        assert isinstance(equipment, Equipment)
        self.__children.append(equipment)

    def remove(self, equipment):
        assert isinstance(equipment, Equipment)
        self.__children.remove(equipment)

    @abstractmethod
    def get_name(self):
        raise NotImplementedError()