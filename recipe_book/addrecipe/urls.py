from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="addrecipe"),
    path("add", views.add, name="add"),


]