class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector2(x={self.x!r}, y={self.y!r})'

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector2(x=self.x*other, y=self.y*other)
        raise TypeError("Unsup")

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        self.x *= other
        self.y *= other

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)


print(Vector2(1, 2) * 3)
print(3 * Vector2(1, 2))
v = Vector2(1, 2)
v *= 3

print(Vector2(1, 2) == Vector2(1, 2))
print(Vector2(1, 2) == Vector2(1, 2))

