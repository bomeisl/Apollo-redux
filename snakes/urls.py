from django.urls import path
from .views import SnakeView

urlpatterns = [
    path('', SnakeView.get, name='snakes')
]