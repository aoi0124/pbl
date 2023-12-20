import MySQLdb

con = MySQLdb.connect(
        host="localhost",
        user="root",
        password="abc",
        db="board",
        charset="utf8mb4"
    )
cur = con.cursor()

cur.execute('''
                CREATE TABLE IF NOT EXISTS user
                (id MEDIUMINT NOT NULL AUTO_INCREMENT,
                 name VARCHAR(30),
                 address VARCHAR(30),
                 password VARCHAR(30),
                 PRIMARY KEY(id))
            ''')
con.commit()
con.close()