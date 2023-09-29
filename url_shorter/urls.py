from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='index'),
    path('generator/', views.generator,name='generator'),
    path('<str:pk>',views.url_redirect,name='url_redirect')
]
