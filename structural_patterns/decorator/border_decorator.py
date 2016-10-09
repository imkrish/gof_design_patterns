from structural_patterns.decorator.decorator import Decorator


class BorderDecorator(Decorator):

    def draw(self):
        return super().draw() + self.add_border()

    def add_border(self):
        return ' |add border|'
