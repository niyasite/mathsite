from django.shortcuts import render, get_object_or_404
from .models import Topic, Step


def topic_list(request):
    topics = Topic.objects.all()
    return render(request, 'lessons/topic_list.html', {'topics': topics})


def step_view(request, topic_id, step_order):
    topic = get_object_or_404(Topic, id=topic_id)

    step = get_object_or_404(
        Step,
        topic=topic,
        order=step_order
    )

    total_steps = Step.objects.filter(topic=topic).count()

    progress = int((step_order / total_steps) * 100)

    next_step = Step.objects.filter(
        topic=topic,
        order=step_order + 1
    ).first()

    previous_step = Step.objects.filter(
        topic=topic,
        order=step_order - 1
    ).first()

    return render(request, 'lessons/step.html', {
        'topic': topic,
        'step': step,
        'next_step': next_step,
        'previous_step': previous_step,
        'total_steps': total_steps,
        'progress': progress,
    })