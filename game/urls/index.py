from django.urls import path, include
from game.views.index import index


urlpatterns = [
    path("", index, name="index"),#总函数，整个游戏的一个入口函数
    path("menu/", include("game.urls.menu.index")),
    path("playground/", include("game.urls.playground.index")),
    path("settings/", include("game.urls.settings.index")),
]
