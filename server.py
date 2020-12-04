from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/<page_name>')
def html_page(page_name):
	return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method=='POST':
		try:
			data = request.form.to_dict()
			print(data)
			write_to_csv(data)
			return redirect('/thankyou.html')
		except:
			return 'Did not save to database'
	else:
		return 'Form had error'

# https://thispointer.com/python-how-to-append-a-new-row-to-an-existing-csv-file/

def write_to_csv(data):
	with open('database.csv', newline='', mode='a+') as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer = csv.writer(database, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subject, message])


# Early stage testing
@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/<username>/<int:post_id>')
def hello_user(username=None,post_id=None):
    return render_template('welcome.html',displayname=username,post_num=post_id)

@app.route('/blog')
def blog():
    return '<h1>These are my thoughts on blogs</h1>'
