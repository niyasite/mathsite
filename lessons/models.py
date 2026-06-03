from django.db import models

class Topic(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Step(models.Model):
    STEP_TYPES = (
        ('image', 'تصویر'),
        ('video', 'ویدیو'),
        ('question', 'سؤال'),
        ('finish', 'پایان'),
    )

    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name='steps'
    )
    title = models.CharField(max_length=200, blank=True)
    step_type = models.CharField(max_length=10, choices=STEP_TYPES)
    order = models.PositiveIntegerField()

    image = models.ImageField(upload_to='lesson_images/', blank=True, null=True)
    video = models.FileField(upload_to='lesson_videos/', blank=True, null=True)

    question = models.TextField(blank=True)
    analysis = models.TextField(blank=True)

    def __str__(self):
        return f"{self.topic.title} - مرحله {self.order}"