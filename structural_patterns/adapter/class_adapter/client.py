from structural_patterns.adapter.class_adapter.shape import Shape
from structural_patterns.adapter.class_adapter.text_shape import TextShape
from structural_patterns.adapter.class_adapter.point import Point


if __name__ == '__main__':
    text_shape = TextShape()
    assert isinstance(text_shape, Shape)
    text_shape.bounding_box(Point(1, 2), Point(5, 10))
    text_shape.create_manipulator()
    text_shape.is_empty()
    print(text_shape)