# Generated by Django 4.1.2 on 2022-11-30 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KHF_app', '0006_alter_user_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='meal_type',
            field=models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Snack', 'Snack'), ('Water', 'Water')], max_length=9),
        ),
    ]
