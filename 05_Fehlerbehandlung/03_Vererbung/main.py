from modelle import Fernseher, Laptop, Smartphone, Tablet
import sys

def main():
    try:
        fernseher = Fernseher("Samsung", "QLED", 120, 55, "4K")
        print(fernseher.info())
        print()
    except Exception as error:
        print(f"Unerwarteter Fehler: {error}")
        sys.exit(1)  # Hochgeblubberter Fehler, nicht behebbar
    try:
        laptop = Laptop("Apple", "MacBook Pro", 85, "M2 Pro", 16)
        print(laptop.info())
        print()
    except Exception as error:
        print(f"Unerwarteter Fehler: {error}")
        sys.exit(1)  # Hochgeblubberter Fehler, nicht behebbar
    try:
        smartphone = Smartphone("Apple", "iPhone 14", 20, 48, 256)
        print(smartphone.info())
        print()
    except Exception as error:
        print(f"Unerwarteter Fehler: {error}")
        sys.exit(1)  # Hochgeblubberter Fehler, nicht behebbar
    try:
        tablet = Tablet("Samsung", "Galaxy Tab S8", 15, 11, 128)
        print(tablet.info())
        print()
    except Exception as error:
        print(f"Unerwarteter Fehler: {error}")
        sys.exit(1)  # Hochgeblubberter Fehler, nicht behebbar
    
    try:
        fernseher.einschalten()
        fernseher.ausschalten()
        print()
        laptop.einschalten()
        laptop.ausschalten()
        print()
        smartphone.einschalten()
        smartphone.ausschalten()
        print()
        tablet.einschalten()
        tablet.ausschalten()
    except Exception as error:
        print(f"Unerwarteter Fehler: {error}")
        sys.exit(1)

if __name__ == "__main__":
    main()