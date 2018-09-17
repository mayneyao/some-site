from django.conf.urls import url, include
from rest_framework import routers

from .views import GifTemplateViewsets

router = routers.DefaultRouter()
router.register(r'tmp', GifTemplateViewsets)

urlpatterns = [
    url(r'^', include(router.urls)),
]
