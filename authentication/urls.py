from django.urls import path
from authentication.views import SignUpViews

urlpatterns = [
    path('SignUp/', SignUpViews.as_view()),
]