from django.urls import path
from projeto_mindtrack import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('cadastro/', views.cadastro, name = 'cadastro'),
    path('login/', views.login, name = 'login'),
    path('perguntas/',views.perguntas, name = 'perguntas'),
]
