from .celery import app
from apps.motivo.models import Profile
from django.core.mail import send_mail


# todo remove hello world task
@app.task
def hello_world():
    print("Hello world")

@app.task
def challenge_mail(fname,lname,chtitle):
    '''Sends email to admin when users attempt to do the challenge
       
       Parameters
       ----------
       fname : str
        User first name
       lname : str
        User last name
       chtitle : str
        Name of the challenge
    '''
    send_mail(f'Motivo - {fname} {lname} attempted the challenge {chtitle}',
    f"Hey!\n\n{fname} {lname} just attempted the challenge {chtitle}.\nPlease review it in admin panel :)\n\nCheers, Motivo!",
    'motivoemailtest@gmail.com',
    ['pahej29016@ecofreon.com'])
    
    return None

@app.task
def reward_mail(fname,lname,awtitle,usernote):
    '''Sends email to admin when users attempt to collect award

       Parameters
       ----------
       fname : str
        User first name
       lname : str
        User last name
       awtitle : str
        Name of the award
       usernote : str
        Additional award description
    '''
    send_mail('Motivo - award was collected',
    f"Hey!\n\n{fname} {lname} wants to collect the award {awtitle}.\n\nIncluded note:\n{usernote}.\n\nCheers, Motivo!",
    'motivoemailtest@gmail.com',
    ['pahej29016@ecofreon.com'])
    
    return None

@app.task

    
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