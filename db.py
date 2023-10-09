import MySQLdb

con = MySQLdb.connect(
    host="localhost",
    user="root",
    password="aoi",
    db="掲示板")
cur = con.cursor()

cur.execute('''
                CREATE TABLE 掲示板.list
            (id MEDIUMINT NOT NULL AUTO_INCREMENT,
             name VARCHAR(30),
             sex CHAR(1),
             PRAIMARY KEY(id))
            ''')

con.commit()

con.close()