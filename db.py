import MySQLdb

con = MySQLdb.connect(
    host='localhost',
    user='root',
    password='abc',
    db='user')
cur = con.cursor()
cur.execute("""
            CREATE TABLE user.list
    (id MEDIUMINT NOT NULL AUTO_INCREMENT,
    name VARCHAR(30),
    address VARCHAR(30),
    passward CHAR(30),
    PRIMARY KEY (id))
            """)
con.commit()

con.close()