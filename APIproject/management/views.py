from django.db.models import Avg
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import University, Course, UniversityCourse
from .serializers import UniversitySerializer, CourseSerializer, UniversityCourseSerializer


class UniversityViewSet(ModelViewSet):
    queryset = University.objects.order_by("name")
    serializer_class = UniversitySerializer
    http_method_names = ["get", "post", "put", "patch", "delete"]
    filter_backends = [SearchFilter]
    search_fields = ['name']

    @action(detail=True, methods=['get'])
    def courses(self, request, pk=None):
        university = self.get_object()
        queryset = university.courses.all()
        serializer = UniversityCourseSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def course_stats(self, request, pk=None):
        university = self.get_object()
        queryset = university.courses.all()
        total_courses = queryset.count()
        average_duration = queryset.aggregate(avg=Avg('duration_weeks'))['avg'] or 0
        return Response({
            "total_courses": total_courses,
            "average_duration": round(average_duration, 1)
        })

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    http_method_names = ["get", "post", "put", "patch", "delete"]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['title']
    filterset_fields = {
        'title': ["exact", "contains"]
    }

class UniversityCourseViewSet(ModelViewSet):
    queryset = UniversityCourse.objects.all()
    serializer_class = UniversityCourseSerializer
    http_method_names = ["get", "post", "put", "patch", "delete"]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['course__title', 'university__name']
    ordering_fields = ['duration_weeks']
    filterset_fields = {
        'course__title': ["exact", "contains"],
        'semester': ["exact", "contains"]
    }