# Generated by Django 4.1.2 on 2022-11-28 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KHF_app', '0002_user_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Other')], default=1),
        ),
    ]
