import unittest
from Vector import Vector


class VectorMethods(unittest.TestCase):
    def test_equal(self):
        a = Vector([8.218, -9.341])
        self.assertEqual(a, a)

    def test_addition(self):
        a = Vector([8.218, -9.341])
        b = Vector([-1.129, 2.111])
        c = a.plus(b)
        d = a + b
        c_coords = [round(x, 3) for x in c.coordinates]

        self.assertIsInstance(c, Vector)
        self.assertIsInstance(d, Vector)
        self.assertListEqual(c_coords, [7.089, -7.230])
        self.assertEqual(c, d)

    def test_minus(self):
        a = Vector([7.119, 8.215])
        b = Vector([-8.223, 0.878])
        c = a.minus(b)
        d = a - b
        c_coords = [round(x, 3) for x in c.coordinates]

        self.assertIsInstance(c, Vector)
        self.assertIsInstance(d, Vector)
        self.assertListEqual(c_coords, [15.342, 7.337])
        self.assertEqual(c, d)

    def test_scalar_multiplication(self):
        a = 7.41
        b = Vector([1.671, -1.012, -0.318])
        c = b.times_scalar(a)
        c_coords = [round(x, 3) for x in c.coordinates]

        self.assertIsInstance(c, Vector)
        self.assertListEqual(c_coords, [12.382, -7.499, -2.356])

    def test_magnitude(self):
        a = Vector([-0.221, 7.437])
        b = a.magnitude()
        self.assertEqual(round(b, 3), 7.440)

        c = Vector([8.813, -1.331, -6.247])
        d = c.magnitude()
        self.assertEqual(round(d, 3), 10.884)

    def test_normalize(self):
        a = Vector([5.581, -2.136])
        b = a.normalized()
        b_coords = [round(x, 3) for x in b.coordinates]
        self.assertIsInstance(b, Vector)
        self.assertListEqual(b_coords, [0.934, -0.357])

        c = Vector([1.996, 3.108, -4.554])
        d = c.normalized()
        d_coords = [round(x, 3) for x in d.coordinates]
        self.assertIsInstance(d, Vector)
        self.assertListEqual(d_coords, [0.34, 0.53, -0.777])

    def test_dot_product(self):
        a = Vector([7.887, 4.138])
        b = Vector([-8.802, 6.776])
        c = a.dot(b)
        self.assertEqual(round(c, 3), -41.382)

        d = Vector([-5.955, -4.904, -1.874])
        e = Vector([-4.496, -8.755, 7.103])
        f = d.dot(e)
        self.assertEqual(round(f, 3), 56.397)

    def test_angle_with(self):
        a = Vector([3.183, -7.627])
        b = Vector([-2.668, 5.319])
        c = a.angle_with(b)
        self.assertEqual(round(c, 3), 3.072)

        d = Vector([7.35, 0.221, 5.188])
        e = Vector([2.751, 8.259, 3.985])
        f = d.angle_with(e, in_degrees=True)
        self.assertEqual(round(f, 3), 60.276)

    def test_is_parallel_to(self):
        a = Vector([-7.579, -7.88])
        b = Vector([22.737, 23.64])
        self.assertTrue(a.is_parallel_to(b))

        a = Vector([-2.029, 9.97, 4.172])
        b = Vector([-9.231, -6.639, -7.245])
        self.assertFalse(a.is_parallel_to(b))

        a = Vector([-2.328, -7.284, -1.214])
        b = Vector([-1.821, 1.072, -2.94])
        self.assertFalse(a.is_parallel_to(b))

        a = Vector([2.118, 4.827])
        b = Vector([0, 0])
        self.assertTrue(a.is_parallel_to(b))

    def test_is_orthogonal_to(self):
        a = Vector([-7.579, -7.88])
        b = Vector([22.737, 23.64])
        self.assertFalse(a.is_orthogonal_to(b))

        a = Vector([-2.029, 9.97, 4.172])
        b = Vector([-9.231, -6.639, -7.245])
        self.assertFalse(a.is_orthogonal_to(b))

        a = Vector([-2.328, -7.284, -1.214])
        b = Vector([-1.821, 1.072, -2.94])
        self.assertTrue(a.is_orthogonal_to(b))

        a = Vector([2.118, 4.827])
        b = Vector([0, 0])
        self.assertTrue(a.is_orthogonal_to(b))

    def test_component_parallel_to(self):
        a = Vector([3.039, 1.879])
        b = Vector([0.825, 2.036])
        c = a.component_parallel_to(b)
        c_coords = [round(x, 3) for x in c.coordinates]
        self.assertIsInstance(c, Vector)
        self.assertListEqual(c_coords, [1.083, 2.672])

        a = Vector([3.009, -6.172, 3.692, -2.51])
        b = Vector([6.404, -9.144, 2.759, 8.718])
        c = a.component_parallel_to(b)
        c_coords = [round(x, 3) for x in c.coordinates]
        self.assertIsInstance(c, Vector)
        self.assertListEqual(c_coords, [1.969, -2.811, 0.848, 2.68])

    def test_component_orthogonal_to(self):
        a = Vector([-9.88, -3.264, -8.159])
        b = Vector([-2.155, -9.353, -9.473])
        c = a.component_orthogonal_to(b)
        c_coords = [round(x, 3) for x in c.coordinates]
        self.assertIsInstance(c, Vector)
        self.assertListEqual(c_coords, [-8.35, 3.376, -1.434])

        a = Vector([3.009, -6.172, 3.692, -2.51])
        b = Vector([6.404, -9.144, 2.759, 8.718])
        c = a.component_orthogonal_to(b)
        c_coords = [round(x, 3) for x in c.coordinates]
        self.assertIsInstance(c, Vector)
        self.assertListEqual(c_coords, [1.04, -3.361, 2.844, -5.19])

    def test_cross_product(self):
        a = Vector([8.462, 7.893, -8.187])
        b = Vector([6.984, -5.975, 4.778])
        c = a.cross(b)
        c_coords = [round(x, 3) for x in c.coordinates]
        self.assertIsInstance(c, Vector)
        self.assertListEqual(c_coords, [-11.205, -97.609, -105.685])

    def test_area_of_parallelogram_with(self):
        a = Vector([-8.987, -9.838, 5.031])
        b = Vector([-4.268, -1.861, -8.866])
        c = a.area_of_parallelogram_with(b)
        self.assertEqual(round(c, 3), 142.122)

    def test_area_of_triangle_with(self):
        a = Vector([1.5, 9.547, 3.691])
        b = Vector([-6.007, 0.124, 5.772])
        c = a.area_of_triangle_with(b)
        self.assertEqual(round(c, 3), 42.565)


if __name__ == '__main__':
    unittest.main()
