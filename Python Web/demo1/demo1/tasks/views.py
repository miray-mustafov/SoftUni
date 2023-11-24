from django.shortcuts import render
from django import http

from demo1.tasks.models import Task



def bare_minimum_view(request):  # htprequest
    return http.HttpResponse('It works')

def show_all_tasks(request):
    all_tasks = Task.objects.all()
    result = ', '.join(f'{t.name}({t.id})' for t in all_tasks)
    return http.HttpResponse(result)

def index(request):
    all_tasks = Task.objects.order_by('id').all()
    context = {
        'title': 'The tasks app!',
        'tasks': all_tasks,
    }
    return render(request, 'index.html', context)
