"""
URL configuration for git1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from movies.views import MovieList, ActionMovies, ComedyMovies, movie_info
from food.views import ItemListViewSet
from register import views as user_views
from django.contrib.auth import views as authentication_views

router = routers.SimpleRouter()
router.register('movies', MovieList)
router.register("action", ActionMovies)
router.register("comedy", ComedyMovies)
router.register("items", ItemListViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("food/", include("food.urls")),
    path("info/", include(router.urls)),
    path("movies/", movie_info),
    path("register/", user_views.user_register, name="user_registration"),
    path("login/", authentication_views.LoginView.as_view(template_name="register/login.html"), name="login"),
    path("logout/", authentication_views.LogoutView.as_view(template_name="register/logout.html"), name="logout")
]
