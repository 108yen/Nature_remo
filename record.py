from six.moves import configparser
import mysql.connector as mydb
import datetime
import get
import pprint

def record(data):
    config = configparser.ConfigParser()
    config.read('conf.txt')

    conn = mydb.connect(
                host='localhost',
                port='3306',
                user=config.get('section','user'),
                password=config.get('section','password'),
                database=config.get('section','dbname')
            )

    conn.ping(reconnect=True)

    cur=conn.cursor()


# db初期設定
    cur.execute("SHOW tables")
    tables=cur.fetchall()
    if not ('hu',) in tables:
        cur.execute("CREATE TABLE hu (val int, created_at datetime)")
    if not ('il',) in tables:
        cur.execute("CREATE TABLE il (val int, created_at datetime)")
    if not ('mo',) in tables:
        cur.execute("CREATE TABLE mo (val int, created_at datetime)")
    if not ('te',) in tables:
        cur.execute("CREATE TABLE te (val int, created_at datetime)")
    conn.commit()

    for k,v in data.items():
        cur.execute("SELECT * FROM "+k+" ORDER BY created_at DESC LIMIT 1")
        newest_data=cur.fetchall()
        if newest_data == [] or not newest_data[0][1] == v['created_at'].replace(tzinfo=None):
            cur.execute("INSERT INTO "+k+" VALUES (%(val)s,%(created_at)s)",v)
    conn.commit()

    # DB操作が終わったらカーソルとコネクションを閉じる
    cur.close()
    conn.close()

if __name__ == '__main__':
    record(get.get())
