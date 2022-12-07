from django.urls import include, path
from rest_framework import routers
from . import views

urlpatterns = [
    # This returns all questions
    path("", views.QuestionList.as_view(), name="question-list"),

    # This returns a question
    path("<int:id>/", views.QuestionDetails.as_view() , name="question-view"),

]


# Index             All questions               GET         /questions          {questions: []}
# Create            Create a new question       POST        /questions          success
# Show              Get xth question            GET         /questions/{id}     {question: {}} 
# Update            Update xth question         PUT         /questions/{id}     success
# Delete            Delete xth question         DELETE      /questions/{id}     success