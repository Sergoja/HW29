from django.urls import path

import users.views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.SimpleRouter()
router.register('location', users.views.LocalViewSet)

urlpatterns = [
    path('', users.views.UserListView.as_view()),
    path('<int:pk>', users.views.UserDetailView.as_view()),
    path('create/', users.views.UserCreateView.as_view()),
    path('<int:pk>/update/', users.views.UserUpdateView.as_view()),
    path('<int:pk>/delete/', users.views.UserDeleteView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view())
]

urlpatterns += router.urls
