from django.contrib import admin

from .models import Question
from .models import Course

admin.site.register(Question)
admin.site.register(Course)