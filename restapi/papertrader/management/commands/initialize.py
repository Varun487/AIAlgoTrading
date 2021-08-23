from django.core.management.base import BaseCommand, CommandError

from services.Initialization.initialize_database import InitializeDatabase


class Command(BaseCommand):
    help = 'Test command'

    def handle(self, *args, **options):
        InitializeDatabase().run()
        self.stdout.write(self.style.SUCCESS('Successfully Initialized DataBase!'))
