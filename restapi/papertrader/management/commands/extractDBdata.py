from django.core.management.base import BaseCommand, CommandError

from services.Initialization.source_and_store_data import source_and_store


class Command(BaseCommand):
    help = 'Test command'

    def handle(self, *args, **options):
        source_and_store()
        self.stdout.write(self.style.SUCCESS('Successfully Sourced and Stored data from database!'))
