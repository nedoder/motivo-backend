from django.core.management.base import BaseCommand, CommandError
from apps.challenges.models import ChallengeCategory

from django.contrib.auth.models import Group
from apps.motivo.models import Profile

class Command(BaseCommand):
    help = 'Assign given user to a group (accepts user email)'
    
    def add_arguments(self, parser):
        parser.add_argument('email', nargs='?', type=str)

    def handle(self, *args, **options):
        email = options['email']
        user = Profile.objects.get(email=email)
        
        # Add user to group
        group = Group.objects.get(name="Budget manager")
        user.groups.add(group)
        
        # Enable login to admin panel
        user.is_staff = True
        user.save()
        
        self.stdout.write(self.style.SUCCESS("User assigned to the budget group!"))