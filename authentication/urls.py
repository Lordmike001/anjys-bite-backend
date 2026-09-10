from django.urls import path
from authentication.views import SignUpViews,LoginViews

urlpatterns = [
    path('SignUp/', SignUpViews.as_view()),
    path('Login/', LoginViews.as_view()),
]