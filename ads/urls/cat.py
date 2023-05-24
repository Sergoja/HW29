import ads.views
from rest_framework import routers

urlpatterns = []

router = routers.SimpleRouter()
router.register('', ads.views.CategoryViewSet)
urlpatterns += router.urls
