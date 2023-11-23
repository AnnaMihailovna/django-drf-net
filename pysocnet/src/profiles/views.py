from rest_framework.generics import RetrieveAPIView

from .models import UserNet
from .serialisers import GetUserNetSerialiser

class GetUserNetView(RetrieveAPIView):
    """
    Вывод профиля пользователя.
    """
    queryset = UserNet.objects.all()
    serializer_class = GetUserNetSerialiser
