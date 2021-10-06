from django.core.management.base import BaseCommand, CommandError
from apps.challenges.models import ChallengeCategory


class Command(BaseCommand):
    help = 'Sets proper categories of challenges'

    def handle(self, *args, **options):
        # Get all the categories
        categories_types = ChallengeCategory.CHALLENGE_CATEGORY_CHOICES
        set_categories = [c.name for c in ChallengeCategory.objects.all()]
        
        # Iterate over all the possible categories
        for category in categories_types:
            if category[0] not in set_categories:
                # Create a category in the database if it doesn't exist
                ChallengeCategory.objects.create(name=category[0])
        
        self.stdout.write(self.style.SUCCESS("ALL CHALLENGE CATEGORIES SET!"))
        