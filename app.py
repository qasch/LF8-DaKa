from flask import Flask, render_template
import sqlite3

# Flask Objekt erzeugen
app = Flask(__name__)


# Routen: die "Wege/URLs", um unsere Funktion
# über den Browser auszuführen
@app.route("/")
@app.route("/index")
def index():
    # Verbindung zur Datenbank herstellen
    # Datenbank erstellen, falls sie nicht existiert
    connection = sqlite3.connect('db/flask.db')

    # Cursor erzeugen
    cursor = connection.cursor()

    # SQL ausführen
    result = cursor.execute(
        """
        SELECT * from person;
        """).fetchall()

    return render_template("index.html", result=result)


@app.route("/about")
def about():
    return "<h1>About Page</h1>"


@app.route("/semantic")
def semantic():
    return render_template("semantic.html")


@app.route("/ueber_uns")
def ueber_uns():
    return render_template("ueber_uns.html")


# Einstiegspunkt in unsere App
# so können wir den Webserver einfach über die IDE starten,
# den Debugging Modus aktivieren etc.
if __name__ == '__main__':
    app.run(debug=True)
