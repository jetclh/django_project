from django.urls import path
from game.views import index, secondpage


urlpatterns = {
    path("", index, name="index"),
    path("secondpage/", secondpage, name="secondpage"),
 }
