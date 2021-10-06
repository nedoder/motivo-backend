# Generated by Django 3.2.7 on 2021-10-05 14:58

import apps.motivo.models
import apps.challenges.validators
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('title', models.CharField(max_length=100)),
                ('collected_coins_gross', models.PositiveIntegerField(default=0)),
                ('collected_coins', models.PositiveIntegerField(default=0)),
                ('initial_budget_gross', models.PositiveIntegerField(default=0, verbose_name='Welcome pack budget')),
                ('annual_budget_gross', models.PositiveIntegerField(default=0)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', apps.motivo.models.ProfileManager()),
            ],
        ),
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('price_in_coins', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/images/')),
                ('number_of_uses', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Awards',
            },
        ),
        migrations.CreateModel(
            name='ChallengeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='uploads/images/')),
            ],
            options={
                'verbose_name': 'Challenge category',
                'verbose_name_plural': 'Challenge category',
            },
        ),
        migrations.CreateModel(
            name='CollectedAwards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_note', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('awards', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='motivo.awards')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Collected Awards',
            },
        ),
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('coins_to_win', models.PositiveIntegerField(default=0)),
                ('description', models.TextField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='uploads/challenge_files/', validators=[apps.challenges.validators.validate_file_size])),
                ('number_of_attempts', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='motivo.challengecategory')),
            ],
        ),
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('confirmed_by_admin', models.BooleanField(default=False)),
                ('file', models.FileField(blank=True, null=True, upload_to='uploads/attempts/')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('challenge', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='attempts', to='motivo.challenge')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'To be approved',
                'verbose_name_plural': 'To be approved',
            },
        ),
    ]
