import sqlite3
import pandas as pd
from datetime import datetime
import os
from settings import DATABASE_NAME

class SportClubDatabase:
    def __init__(self):
        self.conn = sqlite3.connect(DATABASE_NAME)
        self.create_tables()
        self.create_folders()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS leden
            (
                lid_nr INTEGER PRIMARY KEY,
                voornaam TEXT NOT NULL,
                familienaam TEXT NOT NULL,
                telnr TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS registratie
            (
                registratienr INTEGER PRIMARY KEY,
                lid_nr INTEGER,
                timestamp TEXT,
                FOREIGN KEY (lid_nr) REFERENCES leden(lid_nr)
            )
        ''')
        self.conn.commit()

    def create_folders(self):
        os.makedirs('Leden', exist_ok=True)
        os.makedirs('Registratie', exist_ok=True)

    def add_member(self):
        voornaam = input('Voornaam: ')
        familienaam = input('Familienaam: ')
        telnr = input('Telefoonnummer: ')

        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO leden (voornaam, familienaam, telnr)
            VALUES (?, ?, ?)
        ''', (voornaam, familienaam, telnr))
        self.conn.commit()
        print('Lid toegevoegd!')

    def delete_member(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM leden')
        members = cursor.fetchall()

        for member in members:
            print(member)

        lid_nr = input('Geef lidnummer om te verwijderen: ')
        cursor.execute('DELETE FROM leden WHERE lid_nr = ?', (lid_nr,))
        self.conn.commit()
        print('Lid verwijderd!')

    def register(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM leden')
        members = cursor.fetchall()

        if members:
            print('Aanwezige leden:')
            for member in members:
                print(member)
            lid_nr = input('Geef lidnummer om te registreren: ')
            
            timestamp = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')

            cursor.execute('''
                INSERT INTO registratie (lid_nr, timestamp)
                VALUES (?, ?)
            ''', (lid_nr, timestamp))
            self.conn.commit()
            print('Registratie toegevoegd!')
        else:
            print('Geen leden gevonden. Voeg leden toe voordat je probeert te registreren.')

    def export_to_csv(self, filename, query, folder):
        cursor = self.conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()

        if data:
            columns = [description[0] for description in cursor.description]
            df = pd.DataFrame(data, columns=columns)
            timestamp = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
            path = f'{folder}/{filename[:-4]}_{timestamp}.csv'
            df.to_csv(path, index=False)
            print(f'Data geëxporteerd naar {path}')
        else:
            print(f'Geen gegevens gevonden voor query: {query}')

def main():
    sportclub_db = SportClubDatabase()

    while True:
        print("\n1. Voeg lid toe")
        print("2. Verwijder lid")
        print("3. Registreer lid")
        print("4. Exporteer leden naar CSV")
        print("5. Exporteer registratie naar CSV")
        print("6. Exit")

        choice = input("Selecteer een optie: ")

        if choice == '1':
            sportclub_db.add_member()
        elif choice == '2':
            sportclub_db.delete_member()
        elif choice == '3':
            sportclub_db.register()
        elif choice == '4':
            sportclub_db.export_to_csv('leden.csv', 'SELECT * FROM leden', 'Leden')
        elif choice == '5':
            sportclub_db.export_to_csv('registratie.csv', 'SELECT * FROM registratie', 'Registratie')
        elif choice == '6':
            print('Bedankt voor het gebruik van de sportclub app!')
            break
        else:
            print('Ongeldige keuze. Probeer opnieuw.')

if __name__ == "__main__":
    main()
