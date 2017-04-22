## define crondjob

from apscheduler.schedulers.blocking import BlockingScheduler
from schedule.tools import update_periods_database

def update_periods_database_handler():
    # TODO: log results
    update_periods_database()


def run():
    scheduler = BlockingScheduler()

    scheduler.add_job(
        update_periods_database_handler,
        'cron',
        hour='7', minute='13',
        id='update_periods_database_scheduler')

    scheduler.start()
