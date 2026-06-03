from django.contrib import admin
from .models import Topic, Step
class StepInline(admin.TabularInline):
    model = Step
    extra = 1

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    inlines = [StepInline]