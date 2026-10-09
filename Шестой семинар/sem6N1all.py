class Vector:
    def __init__(self, x,y,z):
        assert isinstance(x, (int, float)) and not isinstance(x, bool)
        assert isinstance(y, (int, float)) and not isinstance(x, bool)
        assert isinstance(z, (int, float)) and not isinstance(x, bool)
        self.x = x
        self.y = y
        self.z = z

    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def __add__(self, other):
        assert isinstance(other, Vector)
        return Vector(self.x+other.x, self.y+other.y, self.z+other.z)

    def __sub__(self, other):
        assert isinstance(other, Vector)
        return Vector(self.x-other.x, self.y-other.y, self.z-other.z)

    def __matmul__(self,other):
        if isinstance(other, Vector):
            return (self.x*other.x + self.y*other.y + self.z*other.z)
        elif isinstance(other, (int, float)):
            return Vector(self.x* other, self.y* other, self.z* other)
        else:
            raise AssertionError

    def __str__(self):
        return f'x = {self.x}, y = {self.y}, z = {self.z} '

    def __truediv__(self, other):
        assert isinstance(other, (int, float))
        return Vector(self.x / other, self.y / other, self.z / other)

    def vector_mul(self, other):
        assert isinstance(other, Vector)
        x1 = self.y * other.z - self.z * other.y
        y1 = - self.x * other.z + self.z * other.x
        z1 = self.x * other.y - self.y * other.z
        return Vector(x1, y1, z1)
        


def mass_center(l): #Передаем список векторов
    res = Vector(0, 0, 0)
    for i in l:
        res += i
    return res/len(l)

def area(A, B, C) :
    return abs((B-A).vector_mul(A-C))/2

def max_area(l):
    cur_max = 0
    res = ()

    for i in range(len(l)):
        for j in range(i+1, len(l)):
            for k in range(k+1, len(l)):
                t = area(l[i], l[j], l[k])
                if t > cur_max:
                    cur_max = t
                    res = (l[i], l[j], l[k])
    return cur_max, res