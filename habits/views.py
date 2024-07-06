from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView, get_object_or_404)


from habits.models import Habit
from habits.paginators import CustomPagination

from habits.serializers import HabitSerializer


class HabitCreateAPIView(CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        """Метод получения cоздателя(владельца) привычки."""
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitListAPIView(ListAPIView):
    """Класс для получения списка привычек текущего пользователя."""
    serializer_class = HabitSerializer

    pagination_class = CustomPagination

    def get_queryset(self):
        user = self.request.user
        if not user.is_superuser:
            return Habit.objects.filter(user=user)
        return Habit.objects.all()


class HabitRetrieveAPIView(RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitUpdateAPIView(UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitDestroyAPIView(DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
