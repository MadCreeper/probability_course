import canteen_crawler
import schedule
import time
import datetime

record_hrs = [6,7,8,11,12,13,17,18,19]
def job():
    try:
        cur_hour = datetime.datetime.now().hour
        if cur_hour not in record_hrs:
            print(cur_hour, "not recording")
            return None
        else:
            cur_min = datetime.datetime.now().minute
            print(cur_hour, ':', cur_min, "recording!")
            canteen_crawler.crawl()
    except Exception as e:
        print(e)
        

schedule.every(5).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
