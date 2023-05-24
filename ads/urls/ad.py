from django.urls import path

import ads.views
from rest_framework import routers

urlpatterns = [
    path('<int:pk>/upload_image/', ads.views.AdUploadImageView.as_view())
]

router = routers.SimpleRouter()
router.register('', ads.views.AdViewSet)
urlpatterns += router.urls
