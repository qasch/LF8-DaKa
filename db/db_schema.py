import sqlite3

# Verbindung zur Datenbank herstellen
# Datenbank erstellen, falls sie nicht existiert
connection = sqlite3.connect('flask.db')

# Cursor erzeugen
cursor = connection.cursor()

# SQL ausführen
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS person (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vorname TEXT, 
        name TEXT
        )
    """)

cursor.execute(
    """
    INSERT INTO person 
        (vorname, name) 
    VALUES 
        ("Willi", "Wüterich"),
        ("Tina", "Tempel"),
        ("Lars", "Lusche")
    """)

# Aenderungen übertragen
connection.commit()
# Datenbankverbindung schliessen
connection.close()