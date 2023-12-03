from rest_framework import routers
from .viewsets import FlyViewSet

router = routers.SimpleRouter()

# In this case it is appended to the route of the app's urls
router.register("api-fly",FlyViewSet)
