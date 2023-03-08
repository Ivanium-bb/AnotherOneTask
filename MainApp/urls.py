from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenBlacklistView,
)

from MainApp.views import RegisterView, authentication_test, LogoutView, NotesViewSet

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name="sign_up"),

    path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),

    path('authentication-test/', authentication_test),

    path('logout/', LogoutView.as_view(), name='log_out'),

    path('note/', NotesViewSet.as_view({"post": "create", "get": "list"})),
    path('note/<id>/', NotesViewSet.as_view({"patch": "update", "delete": "destroy", "get": "retrieve"})),

]
