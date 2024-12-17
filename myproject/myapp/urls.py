from django.urls import path
from .views import RollsListView

urlpatterns = [
    path('rolls/', RollsListView.as_view(), name='rolls-list'),
]
