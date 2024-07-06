from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from users.models import User
from users.serializers import UserSerializer

from rest_framework.permissions import AllowAny


class UserCreateApiView(CreateAPIView):
    """Регистрация пользователя."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserRetrieveApiView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateApiView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDestroyApiView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
