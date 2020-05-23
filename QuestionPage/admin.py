from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin

from QuestionPage.models import QuestionPage


class QuestionPageAdmin(admin.ModelAdmin):
    mptt_indent_field = "title"
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(QuestionPage, QuestionPageAdmin)