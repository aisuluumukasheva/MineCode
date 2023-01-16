from django.db import models

# Create your models here.

from main.models import Lesson, Course
from account.models import User

class CommentCourse(models.Model):
    course = models.ForeignKey(Course, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='course_comments', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} -> {self.course}'

class CommentLesson(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='lesson_comments', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} -> {self.lesson}'


class RatingLesson(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='ratings', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
    value = models.IntegerField(choices=[(1,1), (2,2), (3,3), (4,4), (5,5)])

    def __str__(self):
        return f'{self.author} -> {self.lesson}'


class FavoritesCourse(models.Model):
    author = models.ForeignKey(User, related_name='favorites', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='favorites', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} -> {self.course}'
