from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Subject, Question
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','subject', 'qtype', 'topic', 'difficulty', 'created_at')
    list_filter = ('qtype', 'topic', 'difficulty', 'subject')
    search_fields = ('text', 'explanation', 'answer_text')
fieldsets = (
    (None, {'fields': ('subject', 'topic', 'qtype', 'difficulty', 'text')}),
    ('گزینه‌ها (برای MCQ)', {'fields': ('choice_a', 'choice_b', 'choice_c', 'choice_d', 'correct_choice')}),
    ('پاسخ و توضیح', {'fields': ('answer_text', 'explanation')}),
)

def short_text(self, obj):
    return obj.text[:60]
short_text.short_description = 'سوال'
