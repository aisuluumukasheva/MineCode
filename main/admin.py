from django.contrib import admin
from .models import Category, Course, Lesson
from review.models import CommentCourse, RatingLesson, CommentLesson, FavoritesCourse


class RatingInline(admin.TabularInline):
    model = RatingLesson


class CommentInline(admin.TabularInline):
    model = CommentCourse

class CommentLessonInLine(admin.TabularInline):
    model = CommentLesson


class CourseAdmin(admin.ModelAdmin):
    list_display = ['title','category',]
    list_filter = ['category',]
    search_fields = ['status', 'rating']
    inlines = [CommentInline]


    # search_fields = ['status', 'rating']
    # inlines = [CommentInline, RatingInline]

class LessonAdmin(admin.ModelAdmin):
    list_display = ['course', 'average_rating']
    list_filter = ['course',]
    # search_fields = ['course']
    inlines = [RatingInline]

admin.site.register(Category)
# admin.site.register(Course)
admin.site.register(Course, CourseAdmin)
admin.site.register(CommentCourse)
admin.site.register(RatingLesson)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(CommentLesson)
admin.site.register(FavoritesCourse)

