from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/<string:pagename>')
def submit(pagename):
    return render_template(pagename)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data= request.form.to_dict()
			write_to_csv(data)
			return redirect('ThankYou.html')
		except:
			return "Error aaya"
	else:
		return "Error kaiku aaya?"

def write_to_csv(data):
	with open('database.csv', newline='', mode='a') as database:
		Name = data["name"]
		Email = data["email"]
		Subject = data["subject"]
		Message = data["message"]
		csv_writer = csv.writer(database, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([Name, Email, Subject, Message])
