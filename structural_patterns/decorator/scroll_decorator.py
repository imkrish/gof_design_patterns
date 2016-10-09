from structural_patterns.decorator.decorator import Decorator


class ScrollDecorator(Decorator):

    def draw(self):
        return super().draw() + self.add_scroll()

    def add_scroll(self):
        return ' <add scroll>'

