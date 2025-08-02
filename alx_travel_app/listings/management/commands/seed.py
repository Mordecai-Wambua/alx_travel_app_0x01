from django.core.management.base import BaseCommand
from alx_travel_app.listings.models import Listing
from faker import Faker
import random

fake = Faker()


class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        for _ in range(10):
            Listing.objects.create(
                title=fake.sentence(),
                description=fake.paragraph(),
                location=fake.city(),
                price_per_night=round(random.uniform(50, 500), 2),
                available=random.choice([True, False]),
            )
        self.stdout.write(self.style.SUCCESS("Database seeded with sample listings."))
