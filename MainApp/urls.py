from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from MainApp import views
from MainApp.views import RegisterView, LogoutView, NotesViewSet
router = routers.DefaultRouter()
router.register(r'note', views.NotesViewSet, 'note')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='sign_up'),
    path('token/', TokenObtainPairView.as_view(), name='log_in'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='log_out'),
    path('',  include(router.urls))
]


