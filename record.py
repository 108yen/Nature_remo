from six.moves import configparser
import mysql.connector as mydb
import datetime
import get
import pprint

def record(data):
    # print(data)
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

    # data['date']=datetime.datetime.today()
    # cur.execute("INSERT INTO room VALUES (%(hu)s,%(il)s,%(mo)s,%(te)s,%(date)s)",data)
    # conn.commit()

# db初期設定
    cur.execute("SHOW tables")
    tables=cur.fetchall()
    # print(tables)
    if not ('hu',) in tables:
        cur.execute("CREATE TABLE hu (val int, created_at datetime)")
    if not ('il',) in tables:
        cur.execute("CREATE TABLE il (val int, created_at datetime)")
    if not ('mo',) in tables:
        cur.execute("CREATE TABLE mo (val int, created_at datetime)")
    if not ('te',) in tables:
        cur.execute("CREATE TABLE te (val int, created_at datetime)")
    conn.commit()

    # print(datetime.datetime.today())
    for k,v in data.items():
        cur.execute("SELECT * FROM "+k+" ORDER BY created_at DESC LIMIT 1")
        newest_data=cur.fetchall()
        # print('newest_data:'+str(newest_data))
        if newest_data == [] or not newest_data[0][1] == v['created_at'].replace(tzinfo=None):
            print('record '+k)
            # print('databese:'+str(newest_data[0][1]))
            print('getdata:'+str(v['created_at'].replace(tzinfo=None)))
            cur.execute("INSERT INTO "+k+" VALUES (%(val)s,%(created_at)s)",v)
    conn.commit()

    # DB操作が終わったらカーソルとコネクションを閉じる
    cur.close()
    conn.close()

if __name__ == '__main__':
    record(get.get())
