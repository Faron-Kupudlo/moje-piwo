from django.urls import path

from .views import wpisCreateView
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('wpis/nowy', wpisCreateView.as_view(), name='wpis-nowy')

]