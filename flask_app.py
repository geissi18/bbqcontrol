from flask import Flask, render_template, request
from flask import jsonify

app = Flask(__name__)

settemp = 0

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
    if request.method == 'POST':
        def add_message():
		content = request.get_json()
		print content
	return content