from structural_patterns.composite.composite_equipment import CompositeEquipment


class Chassis(CompositeEquipment):

    def __init__(self, net_price):
        super().__init__(net_price)

    def get_name(self):
        return 'Chassis'
