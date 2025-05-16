class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    def speak(self):
        print(f"{self.name} үн чыгарат: {self.sound}")

    def info(self):
        print(f"📌 Аты: {self.name}")
        print(f"📚 Тукуму: {self.species}")
        print(f"🔊 Үнү: {self.sound}")


# Мисал жаныбарлар
def main():
    dog = Animal("Акбар", "Ит", "Гав-гав")
    cat = Animal("Мурка", "Мышык", "Мяу-мяу")
    cow = Animal("Бозу", "Уй", "Му-у-у")

    animals = [dog, cat, cow]

    print("\n=== 🐶 Жаныбарлар жөнүндө маалымат ===")
    for animal in animals:
        animal.info()
        animal.speak()
        print("-" * 30)

if __name__ == "__main__":
    main()
