# vector-math

Linear algebra methods for vectors.

## Example usage

```python
from Vector import Vector

# instance
a = Vector([8.218, -9.341])
print a  # Vector: (Decimal('8.217999999999999971578290569595992565155029296875'), Decimal('-9.3409999999999993036681189551018178462982177734375'))
print a.coordinates  # (Decimal('8.217999999999999971578290569595992565155029296875'), Decimal('-9.3409999999999993036681189551018178462982177734375'))

# equality
a = Vector([8.218, -9.341])
print a == a  # True

# addition
a = Vector([8.218, -9.341])
b = Vector([-1.129, 2.111])
print a.plus(b)  # Vector: (Decimal('7.08899999999999996802557689080'), Decimal('-7.22999999999999909405801190587'))
print a + b  # Vector: (Decimal('7.08899999999999996802557689080'), Decimal('-7.22999999999999909405801190587'))

# minus
a = Vector([7.119, 8.215])
b = Vector([-8.223, 0.878])
print a.minus(b)  # Vector: (Decimal('15.3420000000000005258016244625'), Decimal('7.33699999999999985522691758888'))
print a - b  # Vector: (Decimal('15.3420000000000005258016244625'), Decimal('7.33699999999999985522691758888'))

# scalar_multiplication
a = 7.41
b = Vector([1.671, -1.012, -0.318])
print b.times_scalar(a)  # Vector: (Decimal('12.3821100000000005402078784300'), Decimal('-7.49892000000000022279067479758'), Decimal('-2.35638000000000008138822948922'))

# magnitude
a = Vector([-0.221, 7.437])
print a.magnitude()  # 7.4402829247280646285389593685977160930633544921875

# normalize
a = Vector([5.581, -2.136])
print a.normalized()  # Vector: (Decimal('0.933935214086640295130539147343'), Decimal('-0.357442325262329983594964055642'))

# dot_product
a = Vector([7.887, 4.138])
b = Vector([-8.802, 6.776])
print a.dot(b)  # -41.3822859999999945439839166283

# angle_with
a = Vector([3.183, -7.627])
b = Vector([-2.668, 5.319])
print a.angle_with(b)  # 3.07202630983724755964203723124228417873382568359375
print a.angle_with(b, in_degrees=True)  # 176.014142106822857852753993491

# is_parallel_to
a = Vector([-7.579, -7.88])
b = Vector([22.737, 23.64])
print a.is_parallel_to(b)  # True

# is_orthogonal_to
a = Vector([-7.579, -7.88])
b = Vector([22.737, 23.64])
print a.is_orthogonal_to(b)  # False

# component_parallel_to
a = Vector([3.039, 1.879])
b = Vector([0.825, 2.036])
print a.component_parallel_to(b)  # Vector: (Decimal('1.08260696248446669921320880516'), Decimal('2.67174275832530224589459303452'))

# component_orthogonal_to
a = Vector([-9.88, -3.264, -8.159])
b = Vector([-2.155, -9.353, -9.473])
print a.component_orthogonal_to(b)  # Vector: (Decimal('-8.35008104319576298139037182171'), Decimal('3.37606125428772042918826614535'), Decimal('-1.43374604278118531453872963265'))

# cross_product
a = Vector([8.462, 7.893, -8.187])
b = Vector([6.984, -5.975, 4.778])
print a.cross(b)  # Vector: (Decimal('-11.2045709999999977337168388658'), Decimal('-97.6094439999999908463337305875'), Decimal('-105.685161999999993914045148813'))

# area_of_parallelogram_with
a = Vector([-8.987, -9.838, 5.031])
b = Vector([-4.268, -1.861, -8.866])
print a.area_of_parallelogram_with(b)  # 142.1222214018463319007423706352710723876953125

# area_of_triangle_with
a = Vector([1.5, 9.547, 3.691])
b = Vector([-6.007, 0.124, 5.772])
print a.area_of_triangle_with(b)  # 42.5649373994189375025598565117
```
