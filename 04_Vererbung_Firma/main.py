from mitarbeiter import Mitarbeiter
from abteilungsleiter import Abteilungsleiter
from abteilung import Abteilung
from firma import Firma

def main():
    firma = Firma()

    abteilung1 = Abteilung("Entwicklung")
    abteilung2 = Abteilung("Marketing")

    leiter1 = Abteilungsleiter("Masood", "m", abteilung1)
    abteilung1.set_leiter(leiter1)

    mitarbeiter1 = Mitarbeiter("Gabriel", "m", abteilung1)
    mitarbeiter2 = Mitarbeiter("Max", "m", abteilung1)
    abteilung1.add_mitarbeiter(mitarbeiter1)
    abteilung1.add_mitarbeiter(mitarbeiter2)

    leiter2 = Abteilungsleiter("Lisa", "w", abteilung2)
    abteilung2.set_leiter(leiter2)

    mitarbeiter3 = Mitarbeiter("Eva", "w", abteilung2)
    abteilung2.add_mitarbeiter(mitarbeiter3)

    firma.add_abteilung(abteilung1)
    firma.add_abteilung(abteilung2)

    print("Anzahl Mitarbeiter: ", firma.anzahl_mitarbeiter())
    print("Anzahl Abteilungsleiter: ", firma.anzahl_abteilungsleiter())
    print("Anzahl Abteilungen: ", firma.anzahl_abteilungen())
    groesste_abt = firma.groesste_abteilung()
    print("Größte Abteilung: ", groesste_abt.name)
    frauen, maenner = firma.geschlechterverhaeltnis()
    print(f"Geschlechterverhältnis: {frauen:.2f}% Frauen, {maenner:.2f}% Männer")


if __name__ == "__main__":
    main()