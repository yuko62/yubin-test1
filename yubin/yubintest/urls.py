from django.urls import path
from django.conf.urls import include
from django.contrib.auth import views
from .views import AddressCreateView

urlpatterns = [
    path('', AddressCreateView.as_view(), name='index'),
]