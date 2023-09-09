from rest_framework.viewsets import ModelViewSet
from api_users.models import UserModel
from api_users.serializers import UserModelSerializer


class UserModelView(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = UserModel.objects.all()
