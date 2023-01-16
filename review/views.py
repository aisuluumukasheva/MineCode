from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from .serializers import CommentCourseSerializer, RatingLessonSerializer,CommentLessonSerializer
from .models import CommentCourse, RatingLesson, CommentLesson
from main.permissions import IsAuthorOrReadOnly
from rest_framework.decorators import action


from rest_framework.decorators import api_view  
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from main.models import Course
from .models import FavoritesCourse

User = get_user_model()


class CommentCourseViewSet(ModelViewSet):
    queryset = CommentCourse.objects.all()
    serializer_class = CommentCourseSerializer
    permission_classes = [IsAuthorOrReadOnly]
    
class CommentLessonViewSet(ModelViewSet):
    queryset = CommentLesson.objects.all()
    serializer_class = CommentLessonSerializer
    permission_classes = [IsAuthorOrReadOnly]

class CreateRatingAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=RatingLessonSerializer())
    def post(self, request):
        user = request.user
        ser = RatingLessonSerializer(data=request.data, context={"request":request})
        ser.is_valid(raise_exception=True)
        product_id = request.data.get("product")
        if RatingLesson.objects.filter(author=user, product__id=product_id).exists():
            raiting = RatingLesson.objects.get(author=user, product__id=product_id)
            raiting.value = request.data.get("value")
            raiting.save()
        else:
            ser.save()
        return Response(status=201)


@api_view(['POST'])
def favourite(request):
    author_id = request.data.get('author')
    course_id =request.data.get('course')
    author = get_object_or_404(User, id = author_id)
    course = get_object_or_404(Course , id = course_id)

    if FavoritesCourse.objects.filter(course=course, author=author).exists():
        FavoritesCourse.objects.filter(course=course,author=author).delete()
    else:
        FavoritesCourse.objects.create(course=course,author=author)
    return Response(status=201)

    