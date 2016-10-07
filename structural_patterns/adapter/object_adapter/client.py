from structural_patterns.adapter.object_adapter.shape import Shape
from structural_patterns.adapter.object_adapter.text_shape import TextView
from structural_patterns.adapter.object_adapter.text_shape import TextShape
from structural_patterns.adapter.object_adapter.point import Point


if __name__ == '__main__':
    text_view = TextView()
    text_shape = TextShape(text_view)
    assert isinstance(text_shape, Shape)
    text_shape.bounding_box(Point(1, 2), Point(5, 10))
    text_shape.create_manipulator()
    text_shape.get_text_view().is_empty()
    print(text_shape.get_text_view())