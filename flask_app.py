from flask import Flask, render_template, request

app = Flask(__name__)
#app.config["DEBUG"] = True

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("main.html")

@app.route('/bbqcontrol', methods=["GET", "POST"])
def bbqcontrol():
    if request.method == 'POST':
        #return "This is a POST!"
        settemp = int(request.form["settemp"])
        return "%d" %settemp
        #return redirect(url_for("bbqcontrol"))
    return render_template("bbqcontrol.html")