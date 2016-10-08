from structural_patterns.composite.bus import Bus
from structural_patterns.composite.cabinet import Cabinet
from structural_patterns.composite.card import Card
from structural_patterns.composite.chassis import Chassis
from structural_patterns.composite.composite_equipment import CompositeEquipment
from structural_patterns.composite.equipment import Equipment


if __name__ == '__main__':

    bus = Bus(5)
    print(bus.get_net_price())

    bus.add(Bus(10))
    print(bus.get_net_price())

    card = Card(5)
    bus.add(card)
    print(bus.get_net_price())

    cabinet = Cabinet(10)
    cabinet.add(bus)
    print(cabinet.get_net_price())

    chassis = Chassis(5)
    chassis.add(Card(20))
    cabinet.add(chassis)
    print(cabinet.get_net_price())
    cabinet.remove(bus)
    print(cabinet.get_net_price())