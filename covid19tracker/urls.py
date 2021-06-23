from django.urls import path
from covid19tracker import views

urlpatterns = [
    path('', views.home_view),
]
