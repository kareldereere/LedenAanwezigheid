# Sportclub Applicatie

De Sportclub Applicatie is ontworpen om het beheer van leden en registraties voor een sportclub te vereenvoudigen. 

## Inhoudsopgave
- [Installatie](#installatie)
- [Gebruik van de Applicatie](#gebruik-van-de-applicatie)
- [Structuur van de Applicatie](#structuur-van-de-applicatie)
- [Database](#database)
- [Bestanden en Mappen](#bestanden-en-mappen)

## Installatie

1. Clone de repository naar je lokale machine:

   ```bash
   git clone https://github.com/kareldereere/LedenAanwezigheid.git
   cd LedenAanwezigheid

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python3 main.py


## Gebruik
Voer het programma uit met het volgende commando:

python main.py
Volg de instructies op het scherm om verschillende taken uit te voeren, zoals het toevoegen of verwijderen van leden, registratie van aanwezigheid en exporteren naar CSV

Stappen voor gebruik
Voeg Lid Toe:

Selecteer de optie "Voeg lid toe" in het hoofdmenu.
Voer de gevraagde gegevens in, zoals voornaam, familienaam en telefoonnummer.
Het lid wordt toegevoegd aan de database.
Verwijder Lid:

Kies de optie "Verwijder lid" om een lijst van alle leden te bekijken.
Selecteer het lid dat je wilt verwijderen door het lidnummer in te voeren.
Het gekozen lid wordt uit de database verwijderd.
Registreer Lid:

Selecteer "Registreer lid" om een lijst van alle aanwezige leden te bekijken.
Voer het lidnummer in van het lid dat aanwezig is.
Een registratie wordt toegevoegd met de huidige timestamp.
Exporteer Leden naar CSV:

Kies "Exporteer leden naar CSV" om een CSV-bestand te genereren met alle ledengegevens.
Het bestand wordt opgeslagen in de "Leden" map met een timestamp in de bestandsnaam.
Exporteer Registratie naar CSV:

Selecteer "Exporteer registratie naar CSV" om een CSV-bestand te genereren met registratiegegevens.
Het bestand wordt opgeslagen in de "Registratie" map met een timestamp in de bestandsnaam.
Exit:

Kies "Exit" om de applicatie te verlaten.
Belangrijke Opmerkingen
Zorg ervoor dat je leden toevoegt voordat je registraties uitvoert.
Bij het verwijderen van leden worden alle gerelateerde registraties ook verwijderd.

##Structuur van de applicatie

main.py: Het hoofdprogramma dat de SportClubDatabase-klasse instantieert en de gebruikersinteractie beheert.
settings.py: Bestand voor het opslaan van configuratie-instellingen zoals de database-naam.
venv/: Map voor de virtuele omgeving.
Leden/: Map voor CSV-bestanden met ledengegevens.
Registratie/: Map voor CSV-bestanden met registratiegegevens.

##Database
De applicatie maakt gebruik van een SQLite-database met twee tabellen: leden en registratie. 

##Bestanden en Mappen

leden.csv: CSV-bestand met ledengegevens, gegenereerd na het exporteren van leden.
registratie.csv: CSV-bestand met registratiegegevens, gegenereerd na het exporteren van registratie.

