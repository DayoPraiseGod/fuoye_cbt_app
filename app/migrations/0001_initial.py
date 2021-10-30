# Generated by Django 3.2.5 on 2021-10-15 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('MR', 'MR'), ('MRS', 'MRS'), ('MISS', 'MISS'), ('DR', 'DOCTOR'), ('PROF', 'PROFESSOR')], max_length=10)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
