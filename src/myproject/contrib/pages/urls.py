from django.urls import path
from . import views as v

app_name = "pages"

urlpatterns = [
    path("home/", v.home_view, name="home"),
]
