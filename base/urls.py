from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login",views.login,name = "login"),
    path("register", views.register, name="register"),
    path("all_questions", views.all_questions, name="all_questions"),
    path("sidebar", views.sidebar, name="sidebar"),
    path("user", views.user, name="user"),
    path("add_question",views.add_question, name="add_question"),
    path('update_profile/', views.update_profile, name='update_profile'),
]