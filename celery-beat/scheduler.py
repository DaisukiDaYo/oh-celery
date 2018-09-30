import datetime

from celery import Celery


app = Celery('beat', broker='redis://localhost:6379/0')


@app.task
def print_time():
    print(datetime.datetime.now().strftime('%X'))


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, print_time.signature(), name='print time every 10')
