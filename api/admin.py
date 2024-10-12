from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group
from django.db.models import Count
from api.models import Answer, Question

from unfold.admin import ModelAdmin, TabularInline

# Unregistered to add django-unfold admin
admin.site.unregister(User)
admin.site.unregister(Group)

# Default admin models for django-unfold
@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    pass

@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass

# Answer Inline for Question
class AnswerInline(TabularInline):
    model = Answer
    extra = 4

@admin.register(Question)
class QuestionAdmin(ModelAdmin):
    list_display = ('content', 'level')
    list_filter = ('level',)
    search_fields = ('content',)
    inlines = [AnswerInline]