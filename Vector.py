from math import sqrt, acos, pi
from decimal import Decimal, getcontext

getcontext().prec = 30


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, v):
        return self.plus(v)

    def __sub__(self, v):
        return self.minus(v)

    def plus(self, v):
        return Vector([a + b for a, b in zip(self.coordinates, v.coordinates)])

    def minus(self, v):
        return Vector([a - b for a, b in zip(self.coordinates, v.coordinates)])

    def times_scalar(self, c):
        return Vector([a * Decimal(c) for a in self.coordinates])

    def magnitude(self):
        return Decimal(sqrt(sum([a**2 for a in self.coordinates])))

    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(Decimal('1.0') / Decimal(magnitude))
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    def dot(self, v):
        return sum([a * b for a, b in zip(self.coordinates, v.coordinates)])

    def angle_with(self, v, in_degrees=False):
        def clean_cos(cos_angle):
            return min(1, max(cos_angle, -1))

        u1 = self.normalized()
        u2 = v.normalized()
        angle = Decimal(acos(clean_cos(u1.dot(u2))))

        if(in_degrees):
            angle = angle * Decimal(180.) / Decimal(pi)

        return angle

    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance

    def is_parallel_to(self, v):
        return (
            self.is_zero() or
            v.is_zero() or
            self.angle_with(v) == 0 or
            self.angle_with(v) == pi
        )

    def is_orthogonal_to(self, v, tolerance=1e-10):
        return abs(self.dot(v)) < tolerance

    def component_parallel_to(self, b):
        b_norm = b.normalized()
        proj_mag = self.dot(b_norm)
        return b_norm.times_scalar(proj_mag)

    def component_orthogonal_to(self, b):
        v_para = self.component_parallel_to(b)
        return self - v_para

    def cross(self, v):
        x1, y1, z1 = self.coordinates
        x2, y2, z2 = v.coordinates
        return Vector([
            y1 * z2 - y2 * z1,
            -(x1 * z2 - x2 * z1),
            x1 * y2 - x2 * y1
        ])

    def area_of_parallelogram_with(self, v):
        return self.cross(v).magnitude()

    def area_of_triangle_with(self, v):
        return self.area_of_parallelogram_with(v) / Decimal('2.0')
