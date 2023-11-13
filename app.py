from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app=Flask(__name__,static_folder='./templates/static')
app=Flask(__name__,static_folder="templates", static_url_path='')
# 仮
posts = {
    123: {"post_id": 123, "content": "投稿の内容", "comments": [1, 2, 3]},
    # 他の投稿...
}

comments = {
    1: {"comment_id": 1, "post_id": 123, "text": "コメント1の内容"},
    2: {"comment_id": 2, "post_id": 123, "text": "コメント2の内容"},
    3: {"comment_id": 3, "post_id": 123, "text": "コメント3の内容"},
}

@app.route('/api/posts/<int:post_id>/comments/count', methods=['GET'])
def get_comment_count(post_id):
    post = posts.get(post_id)

    if post:
        comment_count = len(post.get("comments", []))
        return jsonify({"post_id": post_id, "comment_count": comment_count})
    else:
        return jsonify({"error": "Post not found"}), 404
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