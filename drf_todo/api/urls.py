from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = []

router = DefaultRouter()
router.register('tasks', views.TaskViewSet, basename="task")

urlpatterns += router.urls
