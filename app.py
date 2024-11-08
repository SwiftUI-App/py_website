from flask import Flask, render_template_string, url_for, redirect, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_page(
        "Willkommen auf meiner Website!",
        "Hier kannst du meine Python-Apps ausprobieren und mehr über meine Projekte erfahren.",
        "Willkommen auf meiner Startseite! Hier gibt es spannende Projekte und Apps zu entdecken.",
        "home.jpg",  # Bild für die Startseite
        show_apps=True
    )


@app.route('/windows')
def windows():
    return render_page(
        "Windows-Apps",
        "Entdecken Sie die besten Windows-Anwendungen, die ich entwickelt habe. Sie sind benutzerfreundlich und bieten zahlreiche Funktionen!",
        "Diese Seite enthält alle Apps, die ich für Windows entwickelt habe. Perfekt für produktives Arbeiten und Freizeitgestaltung.",
        "windows.jpg",  # Bild für die Windows-Seite
        show_apps=False
    )


@app.route('/macos')
def macos():
    return render_page(
        "MacOS-Apps",
        "Hier finden Sie meine speziell für MacOS entwickelten Anwendungen. Genießen Sie eine nahtlose Integration und erstklassige Leistung!",
        "Meine MacOS-Apps bieten eine nahtlose Benutzererfahrung für Apple-Geräte und sind perfekt auf die Bedürfnisse von Mac-Nutzern abgestimmt. "
        "Klicken Sie auf den untenstehenden Link, um die MacOS-App herunterzuladen.",
        "macos.jpg",  # Bild für die macOS-Seite
        show_apps=False,
        download_link=url_for('static', filename='downloads/gravital.dmg')  # Der Link zur MacOS-App
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Authentifizierung prüfen
        if username == 'Jonathan' and password == 'Rj.120207':
            return redirect('/jonathan')
        else:
            return "Login fehlgeschlagen, bitte versuche es erneut."

    # Wenn GET-Anfrage, dann das Login-Formular anzeigen.
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="de">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Login</title>
            <style>
                body {
                    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #111;  /* Dunkler Hintergrund */
                    display: flex;
                    flex-direction: column;
                    min-height: 100vh;
                    color: white;
                    justify-content: center;
                    align-items: center;
                }
                .login-container {
                    width: 400px;
                    padding: 30px;
                    background-color: #333;
                    border-radius: 10px;
                    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
                    text-align: center;
                }
                .login-container h2 {
                    font-size: 2em;
                    margin-bottom: 20px;
                }
                .login-container label {
                    font-size: 1em;
                    margin-bottom: 10px;
                    display: block;
                    text-align: left;
                }
                .login-container input {
                    width: 100%;
                    padding: 10px;
                    margin-bottom: 20px;
                    border-radius: 5px;
                    border: 1px solid #444;
                    background-color: #222;
                    color: white;
                }
                .login-container button {
                    width: 100%;
                    padding: 10px;
                    border-radius: 5px;
                    border: none;
                    background-color: #007bff;
                    color: white;
                    font-size: 1.1em;
                    cursor: pointer;
                    transition: background-color 0.3s;
                }
                .login-container button:hover {
                    background-color: #0056b3;
                }
            </style>
        </head>
        <body>
            <div class="login-container">
                <h2>Login zu deiner App-Welt</h2>
                <form method="POST">
                    <label for="username">Benutzername:</label>
                    <input type="text" name="username" id="username" required><br>
                    <label for="password">Passwort:</label>
                    <input type="password" name="password" id="password" required><br>
                    <button type="submit">Anmelden</button>
                </form>
            </div>
        </body>
        </html>
    ''')


@app.route('/jonathan')
def jonathan():
    return render_page(
        "Jonathan's Dashboard",
        "Willkommen Jonathan! Hier siehst du deine private Dashboard-Seite.",
        "Dies ist deine personalisierte Seite, die Informationen und Logs anzeigt.",
        "jonathan.jpg",  # Bild für Jonathan
        show_apps=False,
        is_johnny=True  # Flag, um die Terminal-Ansicht anzuzeigen
    )


def render_page(title, header_content, main_content, header_image, show_apps, is_johnny=False, download_link=None):
    logo_url = url_for('static', filename='images/logo.jpg')
    header_image_url = url_for('static', filename=f'images/{header_image}')
    terminal_output = '''$ python3 app.py
[INFO] Server started on http://127.0.0.1:5000
[INFO] User 'Jonathan' logged in
[INFO] Displaying private dashboard'''

    html_content = f'''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #111;  /* Dunkler Hintergrund */
            display: flex;
            flex-direction: column;
            min-height: 100vh;
            color: white;
        }}
        header {{
            background-color: #666;
            color: white;
            padding: 5px 20px;  
            display: flex;
            justify-content: space-between;
            align-items: center;
            height: 50px;
        }}
        .header-left, .header-right {{
            display: flex;
            align-items: center;
        }}
        .logo {{
            width: 50px;
            height: auto;
            cursor: pointer;
            margin-right: 20px;
        }}
        .header-links {{
            display: flex;
            gap: 10px;
        }}
        .header-links a {{
            color: white;
            padding: 5px 10px;
            text-decoration: none;
            font-size: 1em;
            font-weight: 500;
            border-radius: 4px;
            transition: background-color 0.3s, color 0.3s;
        }}
        .header-links a:hover {{
            background-color: #888;
            color: #fff;
        }}
        .login {{
            color: white;
            text-decoration: none;
            font-size: 1em;
            margin-left: 10px;
            padding: 5px 10px;
            border-radius: 4px;
            transition: background-color 0.3s, color 0.3s;
        }}
        .login:hover {{
            background-color: #888;
        }}
        .header-content {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            color: white;
            text-align: center;
            z-index: 10;
        }}
        .header-content h1 {{
            margin: 0;
            font-size: 2.5em;
        }}
        .header-content p {{
            font-size: 1.2em;
        }}
        .image-container {{
            position: relative;
            text-align: center;
            margin: 0;
            overflow: hidden;
            height: 400px;
        }}
        .image-container img {{
            width: 100%;
            height: auto;
            position: relative;
            top: -30%;
            left: 0;
            display: block;
        }}
        main {{
            padding: 20px;
            flex: 1;
        }}
        section {{
            margin-top: 20px;
        }}
        .terminal {{
            background-color: #222;
            padding: 15px;
            border-radius: 5px;
            font-family: 'Courier New', monospace;
            color: #00ff00;
            margin-top: 20px;
            white-space: pre-wrap;  /* Für Zeilenumbruch */
            word-wrap: break-word;   /* Für Zeilenumbruch bei langen Zeilen */
        }}
        footer {{
            background-color: #222;
            padding: 10px;
            text-align: center;
            font-size: 0.9em;
            color: #bbb;
        }}
        .button {{
            display: inline-block;
            padding: 10px 20px;
            background-color: #007bff;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            transition: background-color 0.3s;
        }}
        .button:hover {{
            background-color: #0056b3;
        }}
    </style>
</head>
<body>
    <header>
        <div class="header-left">
            <a href="/">
                <img src="{logo_url}" alt="Logo" class="logo"> 
            </a>
            <div class="header-links">
                <a href="/">Home</a>
                <a href="/windows">Windows</a>
                <a href="/macos">MacOS</a>
            </div>
        </div>
        <div class="header-right">
            <a href="/login" class="login">Anmelden</a>
        </div>
    </header>

    <div class="image-container">
        <img src="{header_image_url}" alt="Header Image">
        <div class="header-content">
            <h1>{title}</h1>
            <p>{header_content}</p>
        </div>
    </div>

    <main>
        <section>
            <p>{main_content}</p>
            {f'<a href="{download_link}" class="button">MacOS App herunterladen</a>' if download_link else ''}
        </section>
        {f'<div class="terminal">{terminal_output}</div>' if is_johnny else ''}
    </main>

    <footer>
        &copy; 2024 Jonathan. Alle Rechte vorbehalten. | <a href="/privacy" style="color: #bbb; text-decoration: none;">Datenschutzerklärung</a> | <a href="/impressum" style="color: #bbb; text-decoration: none;">Impressum</a>
    </footer>
</body>
</html>'''

    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)
