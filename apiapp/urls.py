from django.urls import path
from .views import *

urlpatterns = [
    path("",api_home_page.as_view(),name="home"),
    path("<int:id>/",api_details_page.as_view()),
    path("<int:id>/create/",api_details_page.as_view(),name="home"),
    path("<int:id>/delete/",api_details_page.as_view(),name="home"),
    path("<int:id>/update/",api_details_page.as_view(),name="home")
]
