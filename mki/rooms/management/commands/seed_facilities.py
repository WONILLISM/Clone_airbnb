from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):

    help = "This command tells me that he loves me"

    def handle(self, *args, **options):
        facilites = [
            "Free parking on premises",
            "Gym",
            "Hot tub",
            "Pool",
            "EV charger",
        ]
        for f in facilites:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilites)} facilities created!"))
