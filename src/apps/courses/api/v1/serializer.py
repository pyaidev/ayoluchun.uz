from rest_framework import serializers
from src.apps.courses.models import Course, CourseCategory, CourseVideo, CourseLesson


class CourseListSerializer(serializers.ModelSerializer):
    category_title = serializers.SerializerMethodField('get_category_title')

    def get_category_title(self, obj):
        return obj.category.name

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'image', 'author', 'price', 'discount_price', 'is_discount', 'slug',
                  'category', 'category_title'
                  )


class CourseSingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'author', 'demo_video', 'category', 'description', 'created_at')


class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'id', 'title', 'author', 'description', 'demo_video', 'image', 'price', 'slug',
            'category', 'language', 'is_discount', 'discount_price'
        )


class CourseLessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseLesson
        fields = ('id', 'title', 'description', 'slug', 'course', 'lesson_status',)


class LessonVideoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseVideo
        fields = ('id', 'title', 'video', 'course', 'is_viewed', 'length', 'slug')


class VideoSingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseVideo
        fields = ('id', 'title', 'video', 'course', 'is_viewed', 'length', 'slug')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = ('id', 'name', 'slug')


class CourseLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseVideo
        fields = ['id', 'title', 'course', 'video']
