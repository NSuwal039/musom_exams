# Generated by Django 3.1.7 on 2021-03-15 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0018_auto_20210315_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application_form',
            name='application_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.exam_application'),
        ),
    ]