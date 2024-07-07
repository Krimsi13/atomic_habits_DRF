from celery import shared_task
from habits.services import send_telegram_message
from habits.models import Habit


@shared_task
def send_reminder_of_telegram():
    # message = ""
    # chat_id = habit.owner.tg_id
    pass
