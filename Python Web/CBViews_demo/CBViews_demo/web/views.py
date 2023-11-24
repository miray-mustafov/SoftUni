import random

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import views

from CBViews_demo.web.forms import EmployeeForm, EmployeeModelForm
from CBViews_demo.web.models import Employee, Photo


def home_page_view(request):

    context = {
        'employees': Employee.objects.all()
    }
    return render(request, template_name='home-page.html', context=context)


def register_page_view(request):
    if request.method == "GET":
        form = EmployeeModelForm()
    else:
        form = EmployeeModelForm(request.POST)  # , instance=name
        if form.is_valid():
            # new_user = User.objects.create_user()
            form.save()
            return redirect('home-page')

    context = {
        'form': form,
    }
    return render(request, template_name='register-page.html', context=context)


class HomeView:
    def __init__(self):
        self.values = [2, ]

    @classmethod
    def get_view(cls):
        return cls().view

    def view(self, request):
        return HttpResponse(f'It works!: {self.values}')


class HomeView2(HomeView):
    def __init__(self):
        super().__init__()
        self.values.append(random.randint(16, 30))


class IndexView(views.View):
    def get(self, request):
        return HttpResponse('Etrem aazana get')

    def post(self, request):
        pass


class IndexWithTemplateView(views.generic.TemplateView):
    template_name = 'home-page.html'
    photo = Photo.objects.all()[0]
    extra_context = {
        'title': "TemplateVIEW",
        'employees': Employee.objects.all(),
        'photo': photo,

    }


class EmployeeDetailsView(views.generic.DetailView):
    model = Employee
    template_name = 'details-employee-page.html'
    context_object_name = 'current_employee'


class EmployeeListView(views.generic.ListView):
    pass


class EmployeeCreateView(views.generic.CreateView):
    model = Employee
    fields = '__all__'
    template_name = 'create-employee-page.html'
