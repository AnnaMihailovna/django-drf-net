from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework import permissions

from .models import UserNet
from .serialisers import GetUserNetSerialiser

class GetUserNetView(RetrieveAPIView):
    """
    Вывод профиля пользователя.
    """
    queryset = UserNet.objects.all()
    serializer_class = GetUserNetSerialiser


class UpdateUserNetView(UpdateAPIView):
    """
    Редактирование профиля user.
    """
    serializer_class = GetUserNetSerialiser
    permission_classes = permissions.IsAuthenticated

    def get_queryset(self):
        return UserNet.objects.filter(id=self.request.user.id)