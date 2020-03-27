from apscheduler.schedulers.blocking import BlockingScheduler
from random import choice
from twee import api
from parser import clean_met


sched = BlockingScheduler()

@sched.scheduled_job('interval', hours=6)
def tweet_line():
    print(choice(clean_met))
    api.update_status(choice(clean_met))

sched.start()
