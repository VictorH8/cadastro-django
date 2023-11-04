from django.urls import path
from app_projetocadastro import views


urlpatterns = [
    path('', views.home,name='home'),
    path('usuarios', views.listagem,name='listagem'),
]
