from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! This is the main page lmao <h4>Poopy Poop!</h4>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))
    # Home is the func name it's redirecting to

if __name__ == "__main__":
    app.run()
