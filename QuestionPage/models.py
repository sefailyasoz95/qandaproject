from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class QuestionPage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name="Question Page Title")
    slug = models.SlugField(blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('question_title', kwargs={'slug': self.slug})