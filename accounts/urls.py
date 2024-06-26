from django.urls import path, include

from . import views

app_name = "accounts"
urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("profile/", views.profile, name='profile'),
    path("signup/", views.SignUpView.as_view(), name='signup'),
    path("signin/", views.signin, name='signin'),
]
