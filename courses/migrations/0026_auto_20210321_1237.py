# Generated by Django 3.1.7 on 2021-03-21 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0025_auto_20210321_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='End_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='term',
            name='Start_date',
            field=models.DateField(),
        ),
    ]
