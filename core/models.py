from django.contrib.auth.models import AbstractUser
from django.db import models

class Classroom(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    ]
    middle_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    classroom = models.ManyToManyField('Classroom', related_name='classroom')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)


class Subject(models.Model):
    name = models.CharField(max_length=100)
    user = models.ManyToManyField(CustomUser)
    description = models.TextField()

    def __str__(self):
        return self.name


class Test(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='tests')
    question = models.TextField()
    correct_answer = models.CharField(max_length=255)
    a = models.CharField(max_length=255, blank=True, null=True)
    b = models.CharField(max_length=255, blank=True, null=True)
    c = models.CharField(max_length=255, blank=True, null=True)
    d = models.CharField(max_length=255, blank=True, null=True)
    e = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.subject.name}: {self.question[:50]}"


class StudentResult(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    total_questions = models.PositiveIntegerField()
    correct_answers = models.PositiveIntegerField()
    incorrect_answers = models.PositiveIntegerField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.subject.name}"

