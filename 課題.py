from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return render_template('課題.html')

@app.route('/results', methods=['GET','POST'])
def result():
    if(request.method == 'POST'):
        user_data=request.form
        return render_template('result.html',user_data=user_data)

if __name__ == '__main__':
	app.debug = True
	app.run(host='localhost')