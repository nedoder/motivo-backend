# Generated by Django 3.2.8 on 2021-10-06 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('motivo', '0002_auto_20211006_0913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='category',
        ),
        migrations.DeleteModel(
            name='Attempt',
        ),
        migrations.DeleteModel(
            name='Challenge',
        ),
        migrations.DeleteModel(
            name='ChallengeCategory',
        ),
    ]
