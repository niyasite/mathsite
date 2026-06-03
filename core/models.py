from django.db import models
from django.db import models
from django.core.exceptions import ValidationError


class Subject(models.Model):
    title = models.CharField(max_length=100)

def __str__(self):
    return self.title

class Question(models.Model):
    TOPIC_CHOICES = [
        ('inequality', 'نامعادله'),
        ('identity', 'اتحادها'),
    ]
    QUESTION_TYPES = [
        ('MCQ', 'چندگزینه‌ای'),
        ('TF', 'درست/غلط'),
        ('FILL', 'جای خالی'),
        ('TEXT', 'تشریحی'),
    ]

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    choice_a = models.CharField(max_length=255, blank=True)
    choice_b = models.CharField(max_length=255, blank=True)
    choice_c = models.CharField(max_length=255, blank=True)
    choice_d = models.CharField(max_length=255, blank=True)
    correct_choice = models.CharField(
        max_length=1,
        choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')],
        blank=True,
        null=True)
    answer_text = models.TextField(blank=True)
    explanation = models.TextField(blank=True)
    difficulty = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    qtype = models.CharField(max_length=50, choices=QUESTION_TYPES,default='MCQ')
    topic = models.CharField(max_length=50, choices=TOPIC_CHOICES,default='inequality')

def clean(self):
    super().clean()
    if self.qtype == 'MCQ' and not self.correct_choice:
        raise ValidationError('برای سوال چندگزینه‌ای باید correct_choice مشخص شود.')
    if self.qtype in ['FILL', 'TF','TEXT'] and not self.answer_text:
        raise ValidationError('برای سوال جای خالی باید answer_text مشخص شود.')
def __str__(self):
    return f'{self.subject} - {self.text[:30]}...'
# Create your models here.
