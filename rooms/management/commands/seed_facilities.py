from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):

    help = "create facilities"

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for item in facilities:
            Facility.objects.create(name=item)
        self.stdout.write(self.style.SUCCESS("Facilities created!"))