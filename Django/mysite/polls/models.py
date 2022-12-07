from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_population = models.CharField(max_length=200)

    def __str__(self):
        return self.course_name

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text