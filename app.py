from flask import Flask

# Flask Objekt erzeugen
app = Flask(__name__)


# Routen: die "Wege/URLs", um unsere Funktion
# über den Browser auszuführen
@app.route("/")
@app.route("/index")
def hello_flask():
    return "<h1>Hallo Flask App, jetzt mit Debugger und Start  über IDE!</h1>"


@app.route("/about")
def about():
    return "<h1>About Page</h1>"


# Einstiegspunkt in unsere App
# so können wir den Webserver einfach über die IDE starten,
# den Debugging Modus aktivieren etc.
if __name__ == '__main__':
    app.run(debug=True)
