from flask import Flask, render_template, request
from flask import jsonify

app = Flask(__name__)

settemp = 0
values  = {""}

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("main.html")

@app.route('/bbqcontrol', methods=["GET", "POST"])
def bbqcontrol():
    if request.method == 'POST':
        global settemp
        targettemp = int(request.form["settemp"])
        #Call bbqcontrol_main.py
    return render_template("bbqcontrol.html")

@app.route('/bbqcontrol/settemp')
def temp():
    return jsonify(targettemp=settemp)

@app.route('/bbqcontrol/bbqvalues', methods=["GET", "POST"])
def bbqvalues():
    if request.method == 'POST':
        values = request.get_json(force=True)
        return jsonify(values)
        #print content
    return jsonify(values)
