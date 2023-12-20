from flask import Flask, render_template, request, redirect, url_for, session
import MySQLdb, os

app = Flask(__name__)
app=Flask(__name__,static_folder='./templates/static')
app=Flask(__name__,static_folder="templates", static_url_path='')
app.secret_key = os.urandom(24)

def init_db():
    con = MySQLdb.connect(
        host="localhost",
        user="root",
        password="abc",
        db="board",
        charset="utf8mb4",
        use_unicode=True
    )
    cur = con.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id MEDIUMINT NOT NULL AUTO_INCREMENT,
            name VARCHAR(30),
            address VARCHAR(30),
            password VARCHAR(30),
            PRIMARY KEY(id)
        ) 
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS comments (
            comments_id INTEGER PRIMARY KEY AUTO_INCREMENT,
            user_id MEDIUMINT,
            comment TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES user(id)
        ) 
    ''')
    
    con.commit()
    con.close()


init_db()

@app.route('/', methods=['GET'])
def first():
    return render_template('create.html')

@app.route('/register', methods=['POST'])
def register():
    # フォームからのデータを取得
    name = request.form['name']
    address = request.form['address']
    password = request.form['password']
    
    print("Name:", name)
    print("Address:", address)
    print("Password:", password)
    
    # データベースにデータを挿入
    con = MySQLdb.connect(
        host="localhost",
        user="root",
        password="abc",
        db="board",
        charset="utf8mb4",
        use_unicode=True
    )
    cur = con.cursor()
    cur.execute('INSERT INTO user (name, address, password) VALUES (%s, %s, %s)', (name, address, password))
    con.commit()
	    
    # 登録したデータのIDを取得
    cur.execute("SELECT LAST_INSERT_ID()")
    user_id = cur.fetchone()[0]
    
    con.close()

    return redirect(url_for('login'))

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/result', methods=['POST'])
def result():
    address = request.form['address']
    password = request.form['password']

    con = MySQLdb.connect(
        host="localhost",
        user="root",
        password="abc",
        db="board",
        charset="utf8mb4",
        use_unicode=True
    )
    cur = con.cursor()
    cur.execute("SELECT user.name, comments.comment FROM user INNER JOIN comments ON user.id = comments.user_id")
    comments = cur.fetchall()

    con.close()

    if user_exists(address, password):
        session['user_id'] = get_user_id(address, password)
        return render_template('index.html', comments=comments, title="バスケについての投稿", body="投稿：", bodylist="投稿一覧")
    else:
        return render_template('error.html', message='パスワードかメールアドレスが違っています。')

def user_exists(address, password):
    con = MySQLdb.connect(
        host="localhost",
        user="root",
        password="abc",
        db="board",
        charset="utf8mb4",
        use_unicode=True
    )
    cur = con.cursor()
    cur.execute("SELECT id FROM user WHERE address=%s AND password=%s", (address, password))
    user_id = cur.fetchone()
    con.close()

    return user_id is not None

def get_user_id(address, password):
    con = MySQLdb.connect(
        host="localhost",
        user="root",
        password="abc",
        db="board",
        charset="utf8mb4",
        use_unicode=True
    )
    cur = con.cursor()
    cur.execute("SELECT id FROM user WHERE address=%s AND password=%s", (address, password))
    user_id = cur.fetchone()[0]
    con.close()

    return user_id

@app.route('/post_comment', methods=['POST'])
def post_comment():
    # フォームからのデータを取得
    comment = request.form['comment']
    user_id = session['user_id']
    # データベースにコメントを挿入
    con = MySQLdb.connect(
        host="localhost",
        user="root",
        password="abc",
        db="board",
        charset="utf8mb4",
        use_unicode=True
        )
    cur = con.cursor()
    cur.execute('INSERT INTO comments (user_id, comment) VALUES (%s, %s)', (user_id, comment))
    cur.execute("SELECT LAST_INSERT_ID()")
    comment_id = cur.fetchone()[0]
    
    con.commit()
    con.close()

    return redirect(url_for('index'))

@app.route('/index', methods=['GET'])
def index():
    # データベースからコメントとユーザー名を取得
    con = MySQLdb.connect(
        host="localhost",
        user="root",
        password="abc",
        db="board",
        charset="utf8mb4",
        use_unicode=True
    )
    cur = con.cursor()
    cur.execute("SELECT user.name, comments.comment FROM user INNER JOIN comments ON user.id = comments.user_id")
    comments = cur.fetchall()

    con.close()

    return render_template('index.html', comments=comments, title="バスケについての投稿", body="投稿：", bodylist="投稿一覧")

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')