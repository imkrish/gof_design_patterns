from structural_patterns.adapter.class_adapter.point import Point


class TextView(object):

    def __init__(self):
        self.__origin = None
        self.__width = None
        self.__height = None

    def set_origin(self, x, y):
        self.__origin = Point(x, y)

    def set_extent(self, width, height):
        self.__width = width
        self.__height = height

    def is_empty(self):
        print('is_empty method from text view parent')

    def __repr__(self):
        return 'origin:\t({}, {})\nwidth:\t{}\nheight:\t{}'.format(self.__origin.get_x(),
                                                             self.__origin.get_y(),
                                                             self.__width,
                                                             self.__height)