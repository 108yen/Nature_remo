from six.moves import configparser
import mysql.connector as mydb
import datetime
import get

def record(data):
    config = configparser.ConfigParser()
    config.read('conf.txt')
    # print(config.get('section','user'))

    conn = mydb.connect(
                host='localhost',
                port='3306',
                user=config.get('section','user'),
                password=config.get('section','password'),
                database=config.get('section','dbname')
            )

    conn.ping(reconnect=True)
    # print(conn.is_connected())

    cur=conn.cursor()

    data['date']=datetime.datetime.today()
    cur.execute("INSERT INTO room VALUES (%(hu)s,%(il)s,%(mo)s,%(te)s,%(date)s)",data)
    conn.commit()

    # cur.execute("SELECT * FROM room")
    # print(cur.fetchall())

    # DB操作が終わったらカーソルとコネクションを閉じる
    cur.close()
    conn.close()

if __name__ == '__main__':
    record(get.get())
