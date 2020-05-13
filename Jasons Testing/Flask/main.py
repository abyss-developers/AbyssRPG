from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<name>/")
def user(name):
    return f"Hello {name}"

@app.route("/admin/")
def admin():
    return redirect(url_for("user", name="Admin!"))
    # User is the func name it's redirecting to
    # name="admin" is it passing the parameter

if __name__ == "__main__":
    app.run(debug=True)
