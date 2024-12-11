from flask import Flask, render_template, redirect, url_for, request, session
from user_agents import parse
import datetime

app = Flask(__name__)
app.secret_key = 'mein_geheimer_schluessel'  # Geheimen Schlüssel für die Sitzung

# Liste, um Besucherinformationen zu speichern
visitors = []

@app.route('/')
def home():
    return render_template(
        "home.html",
        title="Willkommen auf meiner Website!",
        header_content="Hier kannst du meine Python-Apps ausprobieren und mehr über meine Projekte erfahren.",
        main_content="Willkommen auf meiner Startseite! Hier gibt es spannende Projekte und Apps zu entdecken.",
        header_image="home.jpg",
        show_apps=True
    )

@app.route('/macos')
def macos():
    return render_template("macos.html")

@app.route('/windows')
def windows():
    return render_template("windows.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "Jonathan" and password == "Rj.120207":
            # Benutzerdaten in der Sitzung speichern
            session['username'] = username
            return redirect('/jonathan')
        else:
            error = "Eingabe prüfen"
    return render_template('login.html', error=error)

@app.route('/jonathan')
def jonathan():
    # Prüfen, ob der Benutzer angemeldet ist
    if 'username' not in session:
        return redirect('/login')  # Weiterleitung zur Login-Seite, wenn nicht eingeloggt
    return render_template('jonathan.html')

@app.route('/dashboard')
def dashboard():
    # Prüfen, ob der Benutzer angemeldet ist
    if 'username' not in session:
        return redirect('/login')  # Weiterleitung zur Login-Seite, wenn nicht eingeloggt

    # IP-Adresse und User-Agent des aktuellen Besuchers
    user_ip = request.remote_addr
    user_agent = parse(request.headers.get('User-Agent'))

    # Geräteinformationen analysieren
    device_type = "Mobile" if user_agent.is_mobile else "Tablet" if user_agent.is_tablet else "Desktop"
    browser = user_agent.browser.family
    os = user_agent.os.family

    # Zeitpunkt des Besuchs
    timestamp = datetime.datetime.now().strftime("%d.%m.%Y, %H:%M")

    # Speichern der Informationen in der Besucher-Liste
    visitors.append({
        "ip": user_ip,
        "device": device_type,
        "browser": browser,
        "os": os,
        "timestamp": timestamp
    })

    return render_template("dashboard.html", visitors=visitors)

@app.route('/datenschutz')
def datenschutz():
    return render_template('datenschutz.html')

# Logout-Route
@app.route('/logout')
def logout():
    # Sitzung löschen, um den Benutzer abzumelden
    session.pop('username', None)
    return redirect('/')

@app.route('/advent')
def advent():
    return render_template("advent.html")

if __name__ == '__main__':
    app.run(debug=True)