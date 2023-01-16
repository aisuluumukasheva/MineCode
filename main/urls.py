from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LessonViewSet, CourseViewSet
from main import views

router = DefaultRouter()
router.register('lessons', LessonViewSet)
router.register('courses', CourseViewSet)

urlpatterns =[
    path('', include(router.urls)),
]
