from punkt_alfa import Point
from named_point import NamedPoint


def main():
    a: NamedPoint = NamedPoint(3, 4, "latarnia")
    print(a)
    a.move(-2, 5)
    print(a)
    print(a.__dict__)
    print(type(a))
    b: NamedPoint = NamedPoint(7, 0, "morze")
    c: Point = Point(5, 9)

    print(issubclass(Point, Point))
    print(issubclass(Point, NamedPoint))
    print(issubclass(NamedPoint, Point))

    print(isinstance(a, Point))
    print(isinstance(a, NamedPoint))
    print(isinstance(c, NamedPoint))
    print(dir(a))
    del a
    print(a)

if __name__ == "__main__":
    main()
