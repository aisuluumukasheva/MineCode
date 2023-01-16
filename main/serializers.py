from rest_framework.serializers import ModelSerializer
from .models import Course,Lesson, Category
from review.serializers import CommentLessonSerializer, CommentCourseSerializer

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        exclude = ('author',)

    def validate(self, attrs):
        attrs =  super().validate(attrs)
        request = self.context.get('request')
        attrs['author'] = request.user
        return attrs

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['favorites'] = instance.favorites.count()
        rep['comments'] = CommentCourseSerializer(instance.comments.all(), many=True).data
        rep['rating'] = instance.average_rating

        return rep

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

    def to_representation(self, instance: Lesson):
        rep = super().to_representation(instance)
        # rep['category'] = CategorySerializer(instance.category).data
        rep['comments'] = CommentLessonSerializer(instance.comments.all(), many=True).data
        rep['rating'] = instance.average_rating
        return rep
