from django.db import models

# Create your models here.
from QuestionPage.models import QuestionPage


class Question(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    LIKED = (
        ('True', 'True'),
        ('False', 'False'),
    )
    questionpage = models.ForeignKey(QuestionPage, on_delete=models.CASCADE, verbose_name="Question Page")
    question = models.TextField(max_length=500, blank=False, verbose_name="question")
    username = models.CharField(max_length=20, blank=True, default="Anonim", verbose_name="username")
    ip = models.CharField(blank=True, max_length=150)
    status = models.CharField(max_length=10, choices=STATUS, default='True')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Likes(models.Model):
    STATUS = (
        ('True', 'Liked'),
        ('False', 'Not Liked'),
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Question")
    count = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS, default="False")
