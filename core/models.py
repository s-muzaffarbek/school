from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('zamdir', 'Zamdirektor'),
        ('director', 'Director'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)


class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'teacher'})
    unique_id = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Test(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='tests')
    question = models.TextField()
    correct_answer = models.CharField(max_length=255)
    options = models.JSONField()

    def __str__(self):
        return f"{self.subject.name}: {self.question[:50]}"


class StudentResult(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    total_questions = models.PositiveIntegerField()
    correct_answers = models.PositiveIntegerField()
    incorrect_answers = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.student.username} - {self.subject.name}"

