from django.urls import include, path
from rest_framework import routers
from . import views

urlpatterns = [
    # This returns all questions
    path("", views.CourseList.as_view(), name="course-list"),

    # This returns a question
    path("<course_name>/", views.CourseDetails.as_view() , name="course-view"),
]


# Index             All questions               GET         /questions          {questions: []}
# Create            Create a new question       POST        /questions          success
# Show              Get xth question            GET         /questions/{id}     {question: {}} 
# Update            Update xth question         PUT         /questions/{id}     success
# Delete            Delete xth question         DELETE      /questions/{id}     success