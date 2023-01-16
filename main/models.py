from django.db import models

from account.models import User


class Category(models.Model):
    title = models.CharField(max_length=70)
    def __str__(self):
        return self.title


class Course(models.Model):
    author = models.ForeignKey(User, related_name='courses', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='courses', on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    description = models.TextField()
    lang = models.CharField(max_length=20, choices=[('english', 'английский'), ('russian', 'русский'), ('kyrgyz', 'кыргызский')])
    level = models.CharField(max_length=20, choices=[('beginner', 'начинающий'), ('advanced', 'продвинутый'), ('professional', 'профи')])
    image = models.ImageField(upload_to='courses')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def average_rating(self):
        lessons = Lesson.objects.filter(course=self)
        values = []
        for lesson in lessons:
            values.append(lesson.average_rating)
        if values:
            return sum(values) / len(values)
        return 0
    
    def __str__(self) -> str:
        return f'{self.author} -> {self.title}'


class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name='lessons', on_delete= models.CASCADE)
    description = models.TextField()
    video = models.FileField(upload_to='lessons')

    @property
    def average_rating(self):
        ratings = self.ratings.all() # это queryset  со значениями ratings
        values = []
        for rating in ratings:
            values.append(rating.value)
        if values:
            return sum(values) / len(values)
        return 0

    class Meta:
        ordering = ['id']  # если в обратном порядке, то ordering = ['-id']

    def __str__(self):
        return f'{self.course}'