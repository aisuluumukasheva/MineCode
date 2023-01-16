from rest_framework.serializers import ModelSerializer

from .models import CommentCourse, CommentLesson, RatingLesson, FavoritesCourse


class CommentCourseSerializer(ModelSerializer):

    class Meta:
        model = CommentCourse
        exclude = ('author',)


    def validate(self, attrs):
        attrs =  super().validate(attrs)
        request = self.context.get('request')
        attrs['author'] = request.user

        return attrs


class CommentLessonSerializer(ModelSerializer):

    class Meta:
        model = CommentLesson
        exclude = ('author',)
        
    
    def validate(self, attrs):
        attrs =  super().validate(attrs)
        request = self.context.get('request')
        attrs['author'] = request.user

        return attrs


class RatingLessonSerializer(ModelSerializer):

    class Meta:
        model = RatingLesson
        exclude = ('author',)


    def validate(self, attrs):
        attrs =  super().validate(attrs)
        request = self.context.get('request')
        attrs['author'] = request.user

        return attrs


class FavoritesCourseSerializer(ModelSerializer):

    class Meta:
        model = FavoritesCourse
        exclude = ('author',)


    def validate(self, attrs):
        attrs =  super().validate(attrs)
        request = self.context.get('request')
        attrs['author'] = request.user

        return attrs