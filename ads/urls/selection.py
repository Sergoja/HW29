import ads.views
from rest_framework import routers

router = routers.SimpleRouter()
router.register('', ads.views.SelectionViewSet)
urlpatterns = router.urls
