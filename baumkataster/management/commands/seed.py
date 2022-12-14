from django.core.management.base import BaseCommand
import random

class Command(BaseCommand):
    help = "seed database for testing and development."

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')

		# TODO: @Helen: Hier deinen Code einfügen!

        self.stdout.write('done.')