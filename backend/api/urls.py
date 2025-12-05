from django.urls import path
from rest_framework import routers

from api import views

app_name = "api"

urlpatterns = [
    path("signup/", views.SignupView.as_view(), name="api_signup"),
    path("login/", views.login_view, name="api_login"),
    path("logout/", views.logout_view, name="api_logout"),
    path("session/", views.session_view, name="api_session"),
    path("whoami/", views.whoami_view, name="api_whoami"),
    path("manual-login/", views.authenticate_view, name="login"),
    path("employees-list/", views.EmployeeView.as_view(), name="employees_list"),
    path(
        r"react-components/<path:path>",
        views.MyReactView.as_view(),
        name="react_app_with_paths",
    ),
    path("", views.index, name="index"),
]

router = routers.DefaultRouter()
router.register("employees", views.EmployeeViewSet, basename="employees")

urlpatterns += router.urls
