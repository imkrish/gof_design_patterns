from structural_patterns.decorator.visual_component import VisualComponent
from structural_patterns.decorator.text_view import TextView
from structural_patterns.decorator.scroll_decorator import ScrollDecorator
from structural_patterns.decorator.border_decorator import BorderDecorator


if __name__ == '__main__':
    visual_component = BorderDecorator(ScrollDecorator(TextView()))
    assert isinstance(visual_component, VisualComponent)
    print(visual_component.draw())