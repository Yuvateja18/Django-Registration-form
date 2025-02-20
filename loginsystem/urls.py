
from django.contrib import admin
from django.urls import path

from myapp import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.register, name="register"),
    path("login/",views.login, name="login"),
    path("logout/",views.logout, name="logout"),
]
