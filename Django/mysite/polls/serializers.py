from rest_framework import serializers
from polls.models import Question
from polls.models import Course


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["question_text", "pub_date"]

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["course_name", "course_number"]
    