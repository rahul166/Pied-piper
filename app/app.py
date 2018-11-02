from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/')
def index():
	lst = ['satyam', 'rahul', 'umesh', 'samarth', 'abhinav', 'ashish', 'yash']
	return render_template("index.html", n = lst)

if (__name__ == "__main__"):
	app.run()