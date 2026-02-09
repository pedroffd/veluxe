from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, TestimonialViewSet

router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'testimonials', TestimonialViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
