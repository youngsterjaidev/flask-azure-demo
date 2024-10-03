from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello Lab11 :)</p>"

@app.route('/add', methods=['GET', 'POST'])
def add_info():
		if request.method == 'POST':
				# store the data in variable
				return "POST"
		else:
				# send all the data in have in a variable
				return "GET"
