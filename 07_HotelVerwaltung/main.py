from hotel import Hotel
from raum import Raum
from einzellzimmer import Einzelzimmer
from doppelzimmer import Doppelzimmer

def main():
    hotel = Hotel("Hotel Post")

    z1 = Einzelzimmer(1)
    z2 = Doppelzimmer(2)
    z3 = Einzelzimmer(3)
    z4 = Doppelzimmer(4)

    for zimmer in [z1, z2, z3, z4]:
        hotel.zimmer_hinzufuegen(zimmer)

    print("Alle Zimmer:")
    print(hotel.zimmer_liste())
    print(hotel.einchecken(2))
    print(hotel.einchecken(3))
    print("Aktuelle Belegung:")
    print(hotel.zimmer_liste())
    print(hotel.auschecken(2))
    print("Aktuelle Belegung:")
    print(hotel.zimmer_liste())

    l = hotel.freie_zimmer()
    print("Freie Zimmer:")
    for z in l:
        print(z)


if __name__ == "__main__":
    main()
