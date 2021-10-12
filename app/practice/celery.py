from celery import Celery
from practice import celeryconfig
from celery.schedules import crontab

app = Celery('practice', broker='amqp://guest:guest@rabbitmq:5672', backend='rpc://',
             include=['practice.tasks'])

app.config_from_object(celeryconfig)

app.conf.beat_schedule = {
    'hello_world': {
        'task': 'practice.tasks.hello_world',
        'schedule': crontab(day_of_month="*", hour="*", minute='*'),
    },
    'reset_annual_budget': {
        'task': 'practice.tasks.reset_annual_budget',
        'schedule': crontab(month_of_year='10', day_of_month="12", hour="13", minute='10')
    }
}

if __name__ == '__main__':
    app.start()
