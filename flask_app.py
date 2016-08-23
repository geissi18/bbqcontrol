from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
#app.config["DEBUG"] = True

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("main.html")

@app.route('/bbqcontrol', methods=["GET", "POST"])
def bbqcontrol():
    if request.method == 'POST':
        #return "This is a POST!"
        return redirect(url_for("bbqcontrol"))
    return render_template("bbqcontrol.html")