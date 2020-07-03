from django.urls import path
from second import views

urlpatterns = [
    path("register/", views.register, name='register'),
    path("personal_page/", views.personal_page, name='personal_page'),
    path("push/", views.push, name='push')
]
