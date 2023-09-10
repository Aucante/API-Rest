from rest_framework.viewsets import ModelViewSet
from api_tasks.models import TaskModel
from api_tasks.serializers import TaskModelSerializer


class TaskModelView(ModelViewSet):
    serializer_class = TaskModelSerializer
    queryset = TaskModel.objects.all()
