from django.urls import path
from .views import (
    FavouriteShow,
    FavouriteChange
)

urlpatterns = [
    path('show/', FavouriteShow.as_view()),
    path('show/<int:todo_id>/', FavouriteChange.as_view())
]
