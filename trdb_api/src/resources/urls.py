from rest_framework import routers

from resources.apps import ResourcesConfig
from resources.views import StudyResourceViewSet, TechnologyViewSet, VoteViewSet

app_name = ResourcesConfig.name

router = routers.DefaultRouter()
router.register(r"study-resources", StudyResourceViewSet, basename="study-resource")
router.register(r"technologies", TechnologyViewSet, basename="technology")
router.register(r"votes", VoteViewSet, basename="vote")

urlpatterns = []
urlpatterns += router.urls
