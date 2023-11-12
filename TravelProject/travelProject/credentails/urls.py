from . import views
from django.urls import path

urlpatterns = [
    path('register',views.registeration,name='registeration'),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout")
]