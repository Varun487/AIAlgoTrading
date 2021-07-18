from django.core.management.base import BaseCommand, CommandError
from services.PaperTradeSynchronizer.papertradesynchronizer import PaperTradeSynchronizer


class Command(BaseCommand):
    help = 'Test command'

    def handle(self, *args, **options):
        PaperTradeSynchronizer().run()
        self.stdout.write(self.style.SUCCESS('Successfully ran Paper Trade Synchronizer!'))
