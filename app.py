from flask import Flask, render_template_string, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_page(
        "Willkommen auf meiner Website!",
        "Hier kannst du meine Python-Apps ausprobieren und mehr über meine Projekte erfahren.",
        "Willkommen auf meiner Startseite! Hier gibt es spannende Projekte und Apps zu entdecken.",
        show_apps=True  # Zeige Apps nur auf der Startseite
    )

@app.route('/windows')
def windows():
    return render_page(
        "Windows-Apps",
        "Entdecken Sie die besten Windows-Anwendungen, die ich entwickelt habe. Sie sind benutzerfreundlich und bieten zahlreiche Funktionen!",
        "Diese Seite enthält alle Apps, die ich für Windows entwickelt habe. Perfekt für produktives Arbeiten und Freizeitgestaltung.",
        show_apps=False  # Zeige Apps hier nicht
    )

@app.route('/macos')
def macos():
    return render_page(
        "MacOS-Apps",
        "Hier finden Sie meine speziell für MacOS entwickelten Anwendungen. Genießen Sie eine nahtlose Integration und erstklassige Leistung!",
        "Meine MacOS-Apps bieten eine nahtlose Benutzererfahrung für Apple-Geräte und sind perfekt auf die Bedürfnisse von Mac-Nutzern abgestimmt.",
        show_apps=False  # Zeige Apps hier nicht
    )

def render_page(title, header_content, main_content, show_apps):
    logo_url = url_for('static', filename='images/logo.png')  # Nutzt Flask's url_for, um den Pfad sicherzustellen
    html_content = f'''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        /* Grundlegende Stile für die Seite */
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f5f5f7;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }}

        header {{
            background-color: #666;
            color: white;
            padding: 10px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
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
            gap: 15px;
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
            display: flex;
            align-items: center;
            color: white;
            text-decoration: none;
            font-size: 1em;
            margin-left: 10px;
        }}

        .profile-icon {{
            width: 24px;
            height: 24px;
            border-radius: 50%;
            background-color: #bbb;
            margin-left: 8px;
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

        ul {{
            list-style-type: none;
            padding: 0;
        }}

        ul li {{
            margin: 10px 0;
        }}

        ul li a {{
            text-decoration: none;
            color: #007bff;
        }}

        ul li a:hover {{
            text-decoration: underline;
        }}

        footer {{
            background-color: #333;
            color: #bbb;
            text-align: center;
            padding: 15px 20px;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <header>
        <div class="header-left">
            <a href="/">
                <img src="{logo_url}" alt="Logo" class="logo"> <!-- Logo-Pfad über url_for definiert -->
            </a>
            <div class="header-links">
                <a href="/">Home</a>
                <a href="/windows">Windows</a>
                <a href="/macos">MacOS</a>
            </div>
        </div>
        <div class="header-right">
            <a href="/login" class="login">Anmelden</a>
            <div class="profile-icon"></div> <!-- Platzhalter-Profilbild -->
        </div>
    </header>

    <div class="image-container">
        <img src="/static/images/header.jpg" alt="Header Bild">
        <div class="header-content">
            <h1>{title}</h1>
            <p>{header_content}</p>
        </div>
    </div>

    <main>
        <section>
            <p>{main_content}</p>
        </section>
        {'<section><h2>Meine Apps</h2><p>Hier kannst du meine Anwendungen ausprobieren:</p><ul><li><a href="/app1">App 1</a></li><li><a href="/app2">App 2</a></li></ul></section>' if show_apps else ''}
    </main>

    <footer>
        &copy; 2024 Deine Website. Alle Rechte vorbehalten. | <a href="/privacy" style="color: #bbb; text-decoration: none;">Datenschutzerklärung</a> | <a href="/impressum" style="color: #bbb; text-decoration: none;">Impressum</a>
    </footer>
</body>
</html>'''
    return render_template_string(html_content)

if __name__ == "__main__":
    app.run(debug=True)
