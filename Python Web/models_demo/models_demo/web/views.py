import random

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from models_demo.web.forms import EmployeeForm, EmployeeModelForm
from models_demo.web.models import Employee

import random
from time import sleep
def slow_operation():
    sleep(5)
    return random.randint(1, 1024)

@cache_page(15)
def index(request):
    value = slow_operation()
    return HttpResponse(value)


def home_page_view(request):
    context = {
        'employees': list(Employee.objects.all())
    }
    return render(request, template_name='home-page.html', context=context)


def register_page_view(request):
    if request.method == "GET":
        form = EmployeeModelForm()
    if request.method == "POST":
        # name = Employee.objects.get_object_or_404(pk=pk)
        form = EmployeeModelForm(request.POST)  # , instance=name
        if form.is_valid():
            form.save()
            #  redirect to the desired page
            # return render(request, template_name='hello-employee-page.html', context={'employee': employee})

    context = {
        'form': form,
    }
    return render(request, template_name='register-page.html', context=context)
