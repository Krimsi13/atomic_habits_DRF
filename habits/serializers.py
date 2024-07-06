from rest_framework.serializers import ModelSerializer

from habits.models import Habit
from habits.validators import (DurationValidator, EnjoyableHabitValidator, RelatedHabitIsEnjoyableValidator,
                               RelatedHabitOrRewardValidator)


class HabitSerializer(ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            RelatedHabitOrRewardValidator(field_1="related_habit", field_2="reward"),
            DurationValidator(field="duration"),
            EnjoyableHabitValidator(),
            RelatedHabitIsEnjoyableValidator(
                field_1="is_enjoyable", field_2="related_habit", field_3="reward"
            ),
        ]

    # def validate(self, data):
    #     duration = data.get('duration')
    #     enjoyable = data.get('is_enjoyable')
    #     related_habit_id = data.get('related_habit_id')
    #     reward = data.get('reward')
    #
    #     if duration is not None:
    #         validate_duration(duration)
    #
    #     if enjoyable is not None:
    #         validate_enjoyable_habit(enjoyable)
    #
    #     if related_habit_id is not None:
    #         validate_related_habit_is_enjoyable(related_habit_id)
    #
    #     if reward is not None:
    #         validate_related_habit_or_reward(reward)
    #
    #     return data

    # def validate(self, data):
    #     RelatedHabitOrRewardValidator()(data)
    #     DurationValidator()(data)
    #     RelatedHabitIsEnjoyableValidator()(data)
    #     EnjoyableHabitValidator()(data)
    #     return data
