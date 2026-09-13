from django.urls import path
from authentication.views import SignUpViews,LoginViews
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('SignUp/', SignUpViews.as_view()),
    path('Login/', LoginViews.as_view()),
    path('refresh/', TokenRefreshView.as_view(), name="token_refresh")
]