from flask import Flask, request

app = Flask(__name__)

# temp variable
user_data = []

@app.route("/")
def hello_world():
    return "<p>Hello Lab11 :)</p>"

@app.route('/add', methods=['GET', 'POST'])
def add_info():
		if request.method == 'POST':
				# fetch the data from the request
				fname = request.form['fname']
				lname = request.form['lname']
				phone = request.form['phone']
				msg = request.form['msg']
				# store the data in variable
				user_data.append({
						"first_name": fname,
						"last_name": lname,
						"phone": phone,
						"msg": msg
				})
				return "POST"
		else:
				# send all the data in have in a variable
				return user_data
