from django.core.management.base import BaseCommand, CommandError
from schedule.models import Period

class Command(BaseCommand):
    help = 'Load schadule from ruz.hse.ru'

    def handle(self, *args, **options):
        print(1)
