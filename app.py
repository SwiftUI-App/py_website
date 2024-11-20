from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

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

@app.route('/windows')
def windows():
    return render_template(
        "windows.html",
        title="Windows-Apps",
        header_content="Entdecken Sie die besten Windows-Anwendungen, die ich entwickelt habe.",
        main_content="Diese Seite enthält alle Apps, die ich für Windows entwickelt habe.",
        header_image="windows.jpg",
        show_apps=False
    )

@app.route('/macos')
def macos():
    return render_template(
        "macos.html",
        title="MacOS-Apps",
        header_content="Hier finden Sie meine speziell für MacOS entwickelten Anwendungen.",
        main_content="Meine MacOS-Apps bieten eine nahtlose Benutzererfahrung.",
        header_image="macos.jpg",
        show_apps=False,
        download_link=url_for('static', filename='downloads/gravital.dmg')
    )

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'Jonathan' and password == 'Rj.120207':
            return redirect('/jonathan')
        else:
            return "Login fehlgeschlagen, bitte versuche es erneut."

    return render_template('login.html')

@app.route('/jonathan')
def jonathan():
    return render_template(
        "jonathan.html",
        title="Jonathan's Dashboard",
        header_content="Willkommen Jonathan! Hier siehst du deine private Dashboard-Seite.",
        main_content="Dies ist deine personalisierte Seite, die Informationen und Logs anzeigt.",
        header_image="jonathan.jpg",
        show_apps=False,
        is_johnny=True
    )

if __name__ == '__main__':
    app.run(debug=True)
