from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=30)

    class Meta:
        ordering = ['course_name']

    def __str__(self):
        return self.course_name

class Educator(models.Model):
    educator_name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course)
    #courses_2 = models.ManyToManyField(Course)


    class Meta:
        ordering = ['educator_name']

    def __str__(self):
        return self.educator_name