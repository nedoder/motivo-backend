# Generated by Django 3.2.8 on 2021-10-08 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0003_annualbudgetmanagement_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annualbudgetmanagement',
            name='category',
            field=models.CharField(choices=[('self-development', 'Self Development'), ('work-accessories', 'Work Accessories'), ('other', 'Other')], default='other', max_length=64),
        ),
    ]
