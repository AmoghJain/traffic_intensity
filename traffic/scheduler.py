import atexit

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import os

from flask import Flask

app = Flask(__name__)


def capture():
    os.system("python screenshot.py")

scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(
    func=capture,
    trigger=IntervalTrigger(minutes=2),
    id='capturing_job',
    name='Captures map every 15 minutes',
    replace_existing=True)
# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())


if __name__ == '__main__':
    app.run(port=7002)
