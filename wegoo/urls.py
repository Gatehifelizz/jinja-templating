from django.urls import path
from wegoo import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inner/', views.inner, name='inner'),
    path('port/', views.portfolio, name='portfolio')
]
