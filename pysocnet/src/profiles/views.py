from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .models import UserNet
from .serialisers import GetUserNetPublicSerializer, GetUserNetSerializer


class UserNetView(ModelViewSet):
    """
    Вывод профиля пользователя.
    """
    serializer_class = GetUserNetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserNet.objects.filter(id=self.request.user.id)


class UserNetPublicView(ModelViewSet):
    """ 
    Вывод публичного профиля пользователя.
    """
    queryset = UserNet.objects.all()
    serializer_class = GetUserNetPublicSerializer
    permission_classes = [permissions.AllowAny]
