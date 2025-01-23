class Auto:
    def __init__(self, ps):
        if not isinstance(ps, (int, float)) or ps < 0:
            raise ValueError("PS muss eine positive Zahl sein")
        self.ps = ps

    def __add__(self, other):
        if not isinstance(other, Auto):
            raise TypeError("Addition nur mit anderen Auto-Objekten möglich")
        return Auto(self.ps + other.ps)

    def __sub__(self, other):
        if not isinstance(other, Auto):
            raise TypeError("Subtraktion nur mit anderen Auto-Objekten möglich")
        return Auto(max(0, self.ps - other.ps))

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("Multiplikation nur mit einer Zahl möglich")
        return Auto(self.ps * other)

    def __truediv__(self, other):
        if not isinstance(other, (int, float)) or other == 0:
            raise ValueError("Division nur mit einer nicht-null Zahl möglich")
        return Auto(self.ps / other)
    
    def __eq__(self, other):
        if not isinstance(other, Auto):
            return False
        return self.ps == other.ps
    
    def __lt__(self, other):
        if not isinstance(other, Auto):
            return False
        return self.ps < other.ps
    
    def __gt__(self, other):
        if not isinstance(other, Auto):
            return False
        return self.ps > other.ps
    
    def __len__(self):
        return int(self.ps)
    
    def __str__(self):
        return f"Auto mit {self.ps} PS"
    
    def __repr__(self):
        return f"Auto({self.ps})"


def main():
    a1 = Auto(50)
    a2 = Auto(60)
    
    print(a1 + a2)  # 110 PS
    print(a2 - a1)  # 10 PS
    print(a1 * 2)   # 100 PS
    print(a2 / 2)   # 30 PS
    
    print(a1 == a2) # False
    print(a1 < a2)  # True
    print(a2 > a1)  # True
    
    print(len(a1))  # 50
    print(repr(a1)) # Auto(50)
    print(str(a2))  # Auto mit 60 PS

if __name__ == "__main__":
    main()
