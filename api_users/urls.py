from rest_framework import routers
from api_users.views import UserModelView

router = routers.DefaultRouter()
router.register(r'users', UserModelView)
