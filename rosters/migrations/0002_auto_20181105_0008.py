# Generated by Django 2.1.2 on 2018-11-05 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='date',
            field=models.DateTimeField(),
        ),
    ]