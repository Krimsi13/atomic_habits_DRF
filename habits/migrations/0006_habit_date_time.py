# Generated by Django 5.0.6 on 2024-07-07 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0005_remove_habit_tg_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="habit",
            name="date_time",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="Время рассылки"
            ),
        ),
    ]
