# Generated by Django 3.2.5 on 2021-10-15 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='email',
            field=models.EmailField(default='email@example.com', max_length=100),
        ),
        migrations.AddField(
            model_name='staff',
            name='password',
            field=models.CharField(default='password', max_length=254),
        ),
    ]
