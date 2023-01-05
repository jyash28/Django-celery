# from app1.models import Widget

from celery import shared_task


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


# @shared_task
# def count_widgets():
#     return Widget.objects.count()
#
#
# @shared_task
# def rename_widget(widget_id, name):
#     w = Widget.objects.get(id=widget_id)
#     w.name = name
#     w.save()

# from celery import shared_task
# from celery.utils.log import get_task_logger
# from time import sleep
# logger = get_task_logger(__name__)
# @shared_task(name='my_first_task')
# def my_first_task(duration):
#     sleep(duration)
#     return('first_task_done')
#
#
# #normal function call in python
# # my_first_task()
# #add task to the celery with function call
# # my_first_task.delay()