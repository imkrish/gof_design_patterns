from structural_patterns.adapter.object_adapter.shape import Shape
from structural_patterns.adapter.object_adapter.text_view import TextView
from structural_patterns.adapter.object_adapter.point import Point


class TextShape(Shape):

    def __init__(self, text_view):
        assert isinstance(text_view, TextView)
        self.__text_view = text_view

    def get_text_view(self):
        return self.__text_view

    def bounding_box(self, bottom_left, top_right):
        assert isinstance(bottom_left, Point) and isinstance(top_right, Point)

        x_left = bottom_left.get_x()
        x_right = top_right.get_x()
        width = x_right - x_left
        x_center = (x_right + x_left) / 2.0

        y_bottom = bottom_left.get_y()
        y_top = top_right.get_y()
        height = y_top - y_bottom
        y_center = (y_top + y_bottom) / 2.0

        self.__text_view.set_origin(x_center, y_center)
        self.__text_view.set_extent(width, height)

    def create_manipulator(self):
        print('Manipulator\'s been created')

    def is_empty(self):
        TextView.is_empty(self.__text_view)
