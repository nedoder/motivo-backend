# Generated by Django 3.0 on 2021-07-20 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motivo', '0008_auto_20210720_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
