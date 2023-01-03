from django.contrib import admin

from .models import Course
from .models import ManuallyAddedCourse

admin.site.register(Course)
admin.site.register(ManuallyAddedCourse)