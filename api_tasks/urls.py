from rest_framework import routers
from api_tasks.views import TaskModelView

router = routers.DefaultRouter()
router.register(r'tasks', TaskModelView)
