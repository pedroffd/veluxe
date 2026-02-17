from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import ServiceViewSet, TestimonialViewSet

router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'testimonials', TestimonialViewSet)

urlpatterns = [
    path('login/', obtain_auth_token),
    path('', include(router.urls)),
]
