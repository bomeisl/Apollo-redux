from django.urls import path
from .views import IndexView

from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('snake_redirect/', IndexView.snake_redirect, name='')
]