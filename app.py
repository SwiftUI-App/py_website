from flask import Flask, render_template, redirect, url_for, request
from user_agents import parse

app = Flask(__name__)

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
            return redirect('/jonathan')
        else:
            error = "Eingabe prüfen"
    return render_template('login.html', error=error)

@app.route('/jonathan')
def jonathan():
    return render_template('jonathan.html')

@app.route('/dashboard')
def dashboard():
    # IP-Adresse und User-Agent des aktuellen Besuchers
    user_ip = request.remote_addr
    user_agent = parse(request.headers.get('User-Agent'))

    # Geräteinformationen analysieren
    device_type = "Mobile" if user_agent.is_mobile else "Tablet" if user_agent.is_tablet else "Desktop"
    browser = user_agent.browser.family
    os = user_agent.os.family

    # Speichere die Infos
    visitors.append({
        "ip": user_ip,
        "device": device_type,
        "browser": browser,
        "os": os
    })

    return render_template("dashboard.html", visitors=visitors)

@app.route('/datenschutz')
def datenschutz():
    return render_template('datenschutz.html')

if __name__ == '__main__':
    app.run(debug=True)
