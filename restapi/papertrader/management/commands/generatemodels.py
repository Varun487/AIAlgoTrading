from django.core.management.base import BaseCommand, CommandError

from services.ModelPredictions.model_generator import ModelGenerator


class Command(BaseCommand):
    help = 'Test command'

    def handle(self, *args, **options):
        ModelGenerator().run()
        self.stdout.write(self.style.SUCCESS('Successfully Generated models!'))
