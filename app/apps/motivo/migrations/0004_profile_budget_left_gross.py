# Generated by Django 3.2.8 on 2021-10-08 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motivo', '0003_auto_20211006_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='budget_left_gross',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
