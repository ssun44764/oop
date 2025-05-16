import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

    def info(self):
        print(f"🔵 Кругдун радиусу: {self.radius}")
        print(f"📐 Аянты (S): {self.area():.2f}")
        print(f"📏 Периметри (L): {self.circumference():.2f}")

def main():
    try:
        r = float(input("Кругдун радиусун киргизиңиз: "))
        if r <= 0:
            print("❗ Радиус оң сан болушу керек.")
            return
        circle = Circle(r)
        print("\n=== Круг жөнүндө маалымат ===")
        circle.info()
    except ValueError:
        print("❗ Радиус сан болушу керек.")

if __name__ == "__main__":
    main()
