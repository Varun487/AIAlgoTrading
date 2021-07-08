from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Test command'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully ran test command!'))
