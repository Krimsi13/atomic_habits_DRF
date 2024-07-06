from datetime import timedelta

from rest_framework.serializers import ValidationError


class RelatedHabitOrRewardValidator:
    """В модели не должно быть заполнено одновременно и поле вознаграждения, и поле связанной привычки.
    Можно заполнить только одно из двух полей."""

    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2

    def __call__(self, value):
        if value.get(self.field_1) and value.get(self.field_2):
            message = f"Невозможно выбрать сразу приятную привычку и вознаграждение"
            raise ValidationError(message)


class DurationValidator:
    """Проверка длительности привычки не более 120 секунд."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.get(self.field) is not None:
            if value.get(self.field) < timedelta(seconds=0):
                message = f"Продолжительность привычки не может быть меньше 0 секунд"
                raise ValidationError(message)
            elif value.get(self.field) > timedelta(seconds=120):
                message = f"Продолжительность привычки не может превышать 120 секунд"
                raise ValidationError(message)


class EnjoyableHabitValidator:
    """Проверка, что связанная привычка является приятной"""

    def __call__(self, habit: dict):
        if related_habit := habit.get("related_habit"):
            if not related_habit.is_enjoyable:
                message = f"Привычка не может быть связанной с вознаграждением"
                raise ValidationError(message)


class RelatedHabitIsEnjoyableValidator:
    """Проверка, что у приятной привычки нет вознаграждения и связанной привычки"""

    def __init__(self, field_1, field_2, field_3):
        self.field_1 = field_1
        self.field_2 = field_2
        self.field_3 = field_3

    def __call__(self, value):
        if (
            value.get(self.field_1)
            and value.get(self.field_2)
            or value.get(self.field_1)
            and value.get(self.field_3)
        ):
            raise ValidationError(
                "У приятной привычки не может быть ни вознаграждения, ни связанной привычки"
            )


# class RelatedHabitOrRewardValidator:
#     def __call__(self, habit):
#         if habit.get("reward") and habit.get("related_habit"):
#             raise ValidationError(
#                 "В модели не должно быть заполнено одновременно и поле вознаграждения, и поле связанной привычки. "
#                 "Можно заполнить только одно из двух полей."
#             )
#
#
# class DurationValidator:
#
#     def __call__(self, habit):
#         if habit.get("duration") and habit.get("duration") > 120:
#             raise ValidationError(
#                 "Время выполнения должно быть не больше 120 секунд"
#             )
#
#
# class RelatedHabitIsEnjoyableValidator:
#
#     def __call__(self, habit):
#         if not habit.get("related_habit"):
#             if habit.get("is_enjoyable"):
#                 raise ValidationError(
#                     "В связанные привычки могут попадать только привычки с признаком приятной привычки."
#                 )
#
#
# class EnjoyableHabitValidator:
#
#     def __call__(self, habit):
#         if habit.get("is_enjoyable") and (
#             habit.get("related_habit") or habit.get("reward")
#         ):
#             raise ValidationError(
#                 "У приятной привычки не может быть вознаграждения или связанной привычки"
#             )
