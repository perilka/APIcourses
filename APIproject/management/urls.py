from rest_framework.routers import DefaultRouter
from django.urls import include, path
from . import views

router = DefaultRouter()
router.register('universities', views.UniversityViewSet)
router.register('courses', views.CourseViewSet)

urlpatterns = [
    path('', include(router.urls))
]