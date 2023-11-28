class Vecteur2D:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def getX(self):
        return self._x

    def setX(self, x):
        self._x = x

    def getY(self):
        return self._y
    
    def setY(self, y):
        self._y = y

    def Tostring(self):
        return f"({self._x}, {self._y})"
    
    def equal(self, other):
        if (self.getX() == other.getX()) and (self.getY() == other.getY()):
            return True
        else:
            return False

    def norme(self):
        return (self._x**2 + self._y**2)**0.5

class Vecteur3D(Vecteur2D):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self._z = z

    def getZ(self):
        return self._z

    def setZ(self, z):
        self._z = z

    def Tostring(self):
        return f"({self._x}, {self._y}, {self._z})"

    def norme(self):
        return (self._x**2 + self._y**2 + self._z**2)**0.5

v2d = Vecteur2D(2, 6)
v12d=Vecteur2D(2,6)
v3d = Vecteur3D(5, 2, 3)


print("v2d:", v2d.Tostring())
print("Norm of v2d:", v2d.norme())
print (v2d.equal(v12d))

print("v3d:", v3d.Tostring())
print("Norm of v3d:", v3d.norme())

