from django.core.management.base import BaseCommand, CommandError
from schedule.models import Period
from schedule.tools import update_periods_database

class Command(BaseCommand):
    help = 'Load schadule from ruz.hse.ru'

    def handle(self, *args, **options):
        update_periods_database()
