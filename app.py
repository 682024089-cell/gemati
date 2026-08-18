from flask import Flask, render_template, redirect, send_from_directory
import os
from flask import url_for

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GAME_FOLDER = os.path.join(BASE_DIR, "game 1")


def resolve_static_folder() -> str:
    candidates = [
        os.path.join(BASE_DIR, "static"),
        os.path.join(BASE_DIR, "api", "static"),
        os.path.join(BASE_DIR, "public", "static"),
    ]
    for candidate in candidates:
        if os.path.isdir(candidate):
            return candidate
    return os.path.join(BASE_DIR, "static")


STATIC_FOLDER = resolve_static_folder()

app = Flask(__name__, static_folder=STATIC_FOLDER, static_url_path="/static", template_folder="templates")


@app.context_processor
def inject_asset_helpers():
    def static_url(path: str) -> str:
        return url_for("static", filename=path)

    return {"static_url": static_url}


@app.route("/favicon.png")
def favicon():
    return app.send_static_file("img/logo.png")


@app.route("/favicon.ico")
def favicon_ico():
    return app.send_static_file("img/logo.png")


@app.route("/video/<path:filename>")
def serve_video(filename):
    return send_from_directory(os.path.join(BASE_DIR, "static", "video"), filename)


@app.route("/")
def index():
    return render_template("home.html")

@app.route("/nama")
def nama():
    return render_template("nama.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")
@app.route("/permainan")
def permainan():
    return render_template("permainan.html")

@app.route("/permainan/penjumlahan")
def permainan_penjumlahan():
    return render_template("permainan_penjumlahan.html")

@app.route("/permainan/simbol/bilangan")
def permainan_simbol_bilangan():
    return render_template("simbol_bilangan.html")

@app.route("/permainan/pengurangan")
def permainan_pengurangan():
    return render_template("permainan_pengurangan.html")

@app.route("/profil")
def profil():
    return render_template("profil.html")

@app.route("/profil/selanjutnya")
def profil_selanjutnya():
    return render_template("profil_selanjutnya.html")

@app.route("/demo")
def demo():
    return render_template("demo.html")

@app.route("/final")
def final():
    return render_template("final.html")

@app.route('/status')
def status():
    return {"status": "ok", "message": "server running"}


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
