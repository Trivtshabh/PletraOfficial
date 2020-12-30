from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('services.html', views.services, name="services"),
    path('pp.html', views.pp, name="pp"),
    path('tc.html', views.tc, name="tc"),
]
