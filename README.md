# baumkataster

Hier werten wir die Daten des Baumkatasters in Bielefeld aus.

## Starten der Anwendung

### Setup

Benötigt werden [Python](https://www.python.org/) und [Node](https://nodejs.org/de/) in Version 16.x (LTS).

Nachdem beide Werkzeuge installiert sind, muss das Projektverzeichnis im Terminal geöffnet werden.
Hier kann überprüft werden, ob alle Tools korrekt installiert wurden:

```
$ python3 --version
Python 3.10.6
$ node -v
v16.17.0
$ npm -v
8.15.0
```

Die Versionen können sich von System zu System unterscheiden, sollten aber nach Möglichkeit diese Versionen haben:

|Software|Version|
|--------|-------|
|Python  |3.10   |
|Node    |16.x   |
|NPM     |8.x    |

### Das Backend einrichten

Anschließend muss die virtuelle Umgebung für Python aktiviert und die benötigten Pakete installiert werden:

```
$ python3 -m venv venv
$ source ./venv/bin/activate (/venv/Script/activate)
$ pip3 install -r requirements.txt
```

Nun kann der Server gestartet werden:

```
$ python3 manage.py runserver (py manage.py runserver)
```

Der Server antwortet uns mit [einer Willkommensnachricht](http://127.0.0.1:8000/hello).

### Das Frontend einrichten

Das Frontend befindet sich im gleichnamigen Ordner `frontend`.
Am besten öffnest du ein neues Terminal und wechselst in diesen Ordner.

Nachdem du in den Ordner gewechselt hast, kannst du auch hier die benötigten Abhängigkeiten installieren:

```
$ npm install
```

Sobald du das erledigt hast, kannst du das Frontend starten:

```
$ npm run start
```

Nach kurzer Wartezeit öffnet sich ein Browser-Fenster und lädt die Seite.

Wenn alles funktioniert, siehst du jetzt eine React-Applikation, die die Nachricht unseres Servers ausgibt.

**Jetzt kann es losgehen!**