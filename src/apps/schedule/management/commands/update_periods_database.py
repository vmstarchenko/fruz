from django.core.management.base import BaseCommand, CommandError
from schedule.models import Period
from schedule.tools import update_periods_database, load_new_audiences

class Command(BaseCommand):
    help = 'Load schadule from ruz.hse.ru'

    def handle(self, *args, **options):
        update_periods_database(load_new_audiences())
