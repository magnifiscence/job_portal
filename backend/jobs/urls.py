from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet, FilterAPIView
from django.views.decorators.cache import cache_page


router = DefaultRouter()
router.register(r'', JobViewSet)

urlpatterns = [
    path('filters/', FilterAPIView.as_view()),
    path('', include(router.urls)),
]