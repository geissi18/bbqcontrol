from flask import Flask, render_template, request
from flask import jsonify

app = Flask(__name__)

settemp = 0
values  = {"firstrun":"1"}

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("main.html")

@app.route('/bbqcontrol', methods=["GET", "POST"])
def bbqcontrol():
    if request.method == 'POST':
        global settemp
        settemp = int(request.form["settemp"])
        #Call bbqcontrol.py
    return render_template("bbqcontrol.html")

@app.route('/bbqcontrol/settemp')
def test():
    return jsonify(temp=settemp)

@app.route('/bbqcontrol/bbqvalues', methods=["GET", "POST"])
def bbqvalues():
	if values("firstrun")==1:
		values = {"actualtemp":"0", "targettemp":"0", "u":"0", "ui_prev":"0", "e_prev":"0", "firstrun":"0"}
    if request.method == 'POST':
        values = request.get_json(force=True)
        return jsonify(values)
        #print content
    return jsonify(values)