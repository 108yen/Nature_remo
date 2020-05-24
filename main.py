#!/usr/local/bin/python3
import record
import get
import schedule
import time

def job():
    record.record(get.get())
    print("do job")

def main():
    # schedule.every().hour.at(":00").do(job)
    # schedule.every().hour.at(":30").do(job)
    schedule.every(10).minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()
