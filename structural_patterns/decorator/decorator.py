from structural_patterns.decorator.visual_component import VisualComponent


class Decorator(VisualComponent):

    def __init__(self, visual_component):
        assert isinstance(visual_component, VisualComponent)
        self.__component = visual_component

    def draw(self):
        return self.__component.draw()
