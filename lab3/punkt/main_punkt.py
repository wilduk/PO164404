from punkt_alfa import Point
from named_point import NamedPoint

def main():
    a: Point = Point(5, 9)
    print(f'Utworzony punkt: {a}')
    a.move(-2, 6)
    print(f'Przesuniety punkt: {a}')
    print(f'Wspolrzedna x: {a.x}, wspolrzedna y: {a.y}')
    print(a.__dict__)
    b = Point(0, 3)
    c = NamedPoint(4, 0, "dworzec")
    print(Point.distance(b, c))


if __name__ == "__main__":
    main()
