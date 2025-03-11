from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = []

router = DefaultRouter()
router.register('tasks', views.TaskViewSet, basename="task")
router.register("projects", views.ProjectViewSet, basename="project")

urlpatterns += router.urls
