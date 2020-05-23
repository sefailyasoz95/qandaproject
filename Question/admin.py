from django.contrib import admin

# Register your models here.
from Question.models import Question, Likes

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'username', 'ip', 'status', 'created_at']

class LikesAdmin(admin.ModelAdmin):
    list_display = ['question', 'count']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Likes, LikesAdmin)
