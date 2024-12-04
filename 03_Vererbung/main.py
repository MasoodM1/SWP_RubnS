from modelle import Fernseher, Laptop, Smartphone, Tablet

def main():
    fernseher = Fernseher("Samsung", "QLED", 120, 55, "4K")
    print(fernseher.info())
    fernseher.einschalten()
    fernseher.ausschalten()
    print()

    laptop = Laptop("Apple", "MacBook Pro", 85, "M2 Pro", 16)
    print(laptop.info())
    laptop.einschalten()
    laptop.ausschalten()

    print()

    smartphone = Smartphone("Apple", "iPhone 14", 20, 48, 256)
    print(smartphone.info())
    smartphone.einschalten()
    smartphone.ausschalten()

    print()

    tablet = Tablet("Samsung", "Galaxy Tab S8", 15, 11, 128)
    print(tablet.info())
    tablet.einschalten()
    tablet.ausschalten()

if __name__ == "__main__":
    main()