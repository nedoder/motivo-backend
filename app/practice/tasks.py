from .celery import app
from apps.motivo.models import Profile

# todo remove hello world task
@app.task
def hello_world():
    print("Hello world")
    
def reset_annual_budget():
    """
    Task resets annual budget when the new year comes.
    The annual budget left is being assigned to a value of annual budget.
    """
    # Get all the users
    profiles = Profile.objects.all()
    
    # Iterate over users and reset their annual budget
    for profile in profiles:
        profile.reset_annual_budget()