from flask import Flask, render_template, request

app = Flask(__name__)
app=Flask(__name__,static_folder='./templates/static')
app=Flask(__name__,static_folder="templates", static_url_path='')

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html',  title="バスケについての投稿",  body="投稿：",  bodylist="投稿一覧")

@app.route('/result', methods=['POST'])
def result():
	email = request.form['email']
	password = request.form['password']
	return render_template('result.html', message = "ログインできました")

@app.route('/create', methods=['POST'])
def create():
	name = request.form['name']
	email = request.form['email']
	password = request.form['password']
	seinengappi = request.form['seinengappi']
	return render_template('result2.html', message = "会員登録しました")

if __name__ == '__main__':
	app.debug = True
	app.run(host='localhost')

