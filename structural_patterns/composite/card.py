from structural_patterns.composite.equipment import Equipment


class Card(Equipment):

    def __init__(self, net_price):
        super().__init__(net_price)

    def get_name(self):
        return 'Card'
