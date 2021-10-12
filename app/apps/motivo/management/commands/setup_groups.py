from django.core.management.base import BaseCommand, CommandError
from apps.challenges.models import ChallengeCategory
from django.contrib.auth.models import Group, Permission
from django.db.utils import IntegrityError

class Command(BaseCommand):
    help = 'Sets proper groups for users'

    def handle(self, *args, **options):
        # Create budget manager group
        try:
            budget_group = Group.objects.create(name='Budget manager')
        except IntegrityError:
            pass
        else:
            budget_permission = Permission.objects.filter(content_type__app_label='budget')
            budget_group.permissions.set(budget_permission)
            budget_group.save()
        
        # Create game manager group
        try:
            game_group = Group.objects.create(name='Game manager')
        except IntegrityError:
            pass
        else:    
            game_permissions = Permission.objects.filter(content_type__app_label__in=['awards', 'challenges', 'motivo'])
            game_group.permissions.set(game_permissions)
            game_group.save()
        
        self.stdout.write(self.style.SUCCESS("Permission groups were created successfully!"))
        