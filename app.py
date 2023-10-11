from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html',  title="バスケについての投稿",  body="投稿：",  bodylist="投稿一覧")

@app.route('/result', methods=['POST'])
def result():
	text=request.form['comment']
	return "<pre>"+text+"</pre>"

if __name__ == '__main__':
	app.debug = True
	app.run(host='localhost')
