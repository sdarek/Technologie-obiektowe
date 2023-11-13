from abc import ABC, abstractmethod
import math


# Interfejs IPolar2D
class IPolar2D(ABC):
    @abstractmethod
    def getAngle(self):
        pass

    @abstractmethod
    def abs(self, param):
        pass


# Interfejs IVector
class IVector(ABC):
    @abstractmethod
    def abs(self):
        pass

    @abstractmethod
    def cdot(self, param):
        pass

    @abstractmethod
    def getComponents(self):
        pass


# Klasa Vector2D implementująca IVector
class Vector2D(IVector):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = 0

    def abs(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def cdot(self, param):
        return self.x * param.x + self.y * param.y

    def getComponents(self):
        return [self.x, self.y]


# Klasa Polar2DAdapter implementująca IVector
class Polar2DAdapter(IPolar2D, IVector):
    def __init__(self, srcVector):
        self.srcVector = srcVector

    def abs(self):
        return self.srcVector.abs()

    def getAngle(self):
        # Implementacja kąta między osią OX a wektorem w układzie biegunowym
        x, y = self.srcVector.getComponents()
        return math.atan2(y, x)

    def cdot(self, param):
        return self.srcVector.cdot(param)

    def getComponents(self):
        return self.srcVector.getComponents()


# Klasa Vector3DInheritance rozszerzająca IVector
class Vector3DInheritance(Vector2D):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def abs(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def cdot(self, param):
        return self.x * param.x + self.y * param.y + self.z * param.z

    def getComponents(self):
        return [self.x, self.y, self.z]

    def cross(self, param):
        # Iloczyn wektorowy dla wektorów trójwymiarowych
        return Vector3DInheritance(
            self.y * param.z - self.z * param.y,
            self.z * param.x - self.x * param.z,
            self.x * param.y - self.y * param.x
        )

    def getSrc(self):
        return Vector2D(self.x, self.y)


# Klasa 2DPolarInheritance rozszerzająca Vector2D
class Polar2DInheritance(Vector2D):
    def getAngle(self):
        return math.atan2(self.y, self.x)  # Kąt między osią OX a wektorem w układzie biegunowym


# Klasa Vector3DDecorator dekorująca IVector
class Vector3DDecorator(IVector):
    def __init__(self, srcVector, z):
        self.srcVector = srcVector
        self.z = z

    def abs(self):
        return math.sqrt(self.srcVector.abs() ** 2 + self.z ** 2)

    def cdot(self, param):
        return self.srcVector.cdot(param) + self.z * param.z

    def getComponents(self):
        return self.srcVector.getComponents() + [self.z]

    def cross(self, param):
        # Iloczyn wektorowy dla wektorów trójwymiarowych
        return Vector3DInheritance(
            self.srcVector.y * param.z - self.srcVector.z * param.y,
            self.srcVector.z * param.x - self.srcVector.x * param.z,
            self.srcVector.x * param.y - self.srcVector.y * param.x
        )

    def getSrcV(self):
        return self.srcVector


# Funkcja main() do testowania
def main():
    # Tworzenie trzech przykładowych wektorów
    wektor1 = Vector3DInheritance(3, 4, 5)
    wektor2 = Vector3DInheritance(1, 2, 3)
    wektor3 = Vector2D(2, 3)

    # Wyświetlanie współrzędnych w układach kartezjańskim
    print("Wektor 1 (Kartezjański):", wektor1.getComponents())
    print("Wektor 2 (Kartezjański):", wektor2.getComponents())
    print("Wektor 3 (Kartezjański):", wektor3.getComponents())

    # Wyświetlanie współrzędnych w układach biegunowym
    biegunowy1 = Polar2DInheritance(wektor1.x, wektor1.y)
    biegunowy2 = Polar2DInheritance(wektor2.x, wektor2.y)
    biegunowy3 = Polar2DInheritance(wektor3.x, wektor3.y)
    print("Wektor 1 (Biegunowy): abs={}, kąt={}".format(biegunowy1.abs(), biegunowy1.getAngle()))
    print("Wektor 2 (Biegunowy): abs={}, kąt={}".format(biegunowy2.abs(), biegunowy2.getAngle()))
    print("Wektor 3 (Biegunowy): abs={}, kąt={}".format(biegunowy3.abs(), biegunowy3.getAngle()))

    # Wyświetlanie wyników iloczynu skalarnego
    iloczyn_skalarny_1_2 = wektor1.cdot(wektor2)
    iloczyn_skalarny_1_3 = wektor1.cdot(wektor3)
    iloczyn_skalarny_2_3 = wektor2.cdot(wektor3)
    print("Iloczyn Skalarny (1, 2):", iloczyn_skalarny_1_2)
    print("Iloczyn Skalarny (1, 3):", iloczyn_skalarny_1_3)
    print("Iloczyn Skalarny (2, 3):", iloczyn_skalarny_2_3)

    # Wyświetlanie wyników iloczynu wektorowego
    iloczyn_wektorowy_1_2 = wektor1.cross(wektor2)
    iloczyn_wektorowy_1_3 = wektor1.cross(wektor3)
    iloczyn_wektorowy_2_3 = wektor2.cross(wektor3)
    print("Iloczyn Wektorowy (1, 2):", iloczyn_wektorowy_1_2.getComponents())
    print("Iloczyn Wektorowy (1, 3):", iloczyn_wektorowy_1_3.getComponents())
    print("Iloczyn Wektorowy (2, 3):", iloczyn_wektorowy_2_3.getComponents())

    # Test iloczynu wektorowego w Vector3DDecorator
    decorated_vector = Vector3DDecorator(wektor1, 2)
    iloczyn_wektorowy_decorated = decorated_vector.cross(wektor3)
    print("Iloczyn Wektorowy Dekorator (1, 3):", iloczyn_wektorowy_decorated.getComponents())


if __name__ == "__main__":
    main()
