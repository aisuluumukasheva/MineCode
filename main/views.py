from rest_framework.viewsets import ModelViewSet


from .serializers import CourseSerializer,LessonSerializer
from .models import Course,Lesson

from .permissions import IsMentor, IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    def get_permissions(self):
        if self.action in ['retrive', 'list', 'search']:
            return [IsAuthorOrReadOnly()]
        return [IsMentor()]



class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_permissions(self):
        if self.action in ['retrive', 'list', 'search']:
            return [IsAuthorOrReadOnly()]
        return [IsMentor()]

    @action(['GET'], detail=False)
    def search(self, request):
        q = request.query_params.get('q')

        if q:
            queryset = queryset.filter(Q(title__icontains=q) | Q(author__first_name__icontains=q) | Q(author__last_name__icontains=q))

        pagination = self.paginate_queryset(queryset)
        if pagination:
            serializer = self.get_serializer(pagination, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=200)
