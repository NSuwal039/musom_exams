# Generated by Django 3.1.7 on 2021-03-21 06:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0024_auto_20210321_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='term',
            name='End_date',
            field=models.DateField(default=datetime.date(2021, 3, 21)),
        ),
        migrations.AddField(
            model_name='term',
            name='Start_date',
            field=models.DateField(default=datetime.date(2021, 3, 21)),
        ),
        migrations.AlterField(
            model_name='application_form',
            name='application_date',
            field=models.DateField(default=datetime.date(2021, 3, 21)),
        ),
    ]