from django.urls import path
from .views import webhook

urlpatterns = [
    path('hooks', webhook)
]
