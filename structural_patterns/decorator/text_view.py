from structural_patterns.decorator.visual_component import VisualComponent


class TextView(VisualComponent):

    def draw(self):
        return 'Text View'
