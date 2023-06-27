from django.urls import path
from rest_framework import routers

from accounts.apps import AccountsConfig
from accounts.views import DetailAPIView, LoginAPIView, LogoutAPIView

app_name = AccountsConfig.name

router = routers.DefaultRouter()

urlpatterns = [
    path("detail/", DetailAPIView.as_view(), name="detail"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("logout/", LogoutAPIView.as_view(), name="logout"),
]
urlpatterns += router.urls
