import os
from apscheduler.schedulers.blocking import BlockingScheduler

def some_job():
    os.system("python movie.py")
    os.system("python tvshows.py")

scheduler = BlockingScheduler()
scheduler.add_job(some_job, 'interval', hours=24)
scheduler.start()
