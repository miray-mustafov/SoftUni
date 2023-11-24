from django.shortcuts import render, redirect

from mid_exam.web.forms import ProfileCreateForm, CarCreateForm, CarEditForm, CarDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from mid_exam.web.models import Profile, Car


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def index(request):
    profile = get_profile()
    context = {'profile': profile}
    return render(request, template_name='index.html', context=context)


def catalogue(request):
    cars = Car.objects.all()
    profile = get_profile()

    context = {'cars': cars, 'cars_count': cars.count(), 'profile': profile}
    return render(request, template_name='catalogue.html', context=context)


def profile_create(request):
    if get_profile():
        return redirect('catalogue')
    if request.method == "GET":
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {'form': form, }
    return render(request, template_name='profile-create.html', context=context)


def profile_details(request):
    profile = get_profile()
    total_price_of_cars = sum([car.price for car in list(Car.objects.all())])

    context = {'profile': profile, 'total_price_of_cars': total_price_of_cars, }
    return render(request, template_name='profile-details.html', context=context)


def profile_edit(request):
    profile = get_profile()
    if request.method == "GET":
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {'form': form, 'profile': profile}
    return render(request, template_name='profile-edit.html', context=context)


def profile_delete(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        # if_form is valid ?
        form.save()
        return redirect('index')

    context = {'form': form, 'profile': profile}
    return render(request, template_name='profile-delete.html', context=context)


def car_create(request):
    profile = get_profile()
    if request.method == 'GET':
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {'form': form, 'profile': profile}
    return render(request, template_name='car-create.html', context=context)


def car_details(request, pk):
    profile = get_profile()
    car = Car.objects.get(pk=pk)

    context = {'car': car, 'profile': profile}
    return render(request, template_name='car-details.html', context=context)


def car_edit(request, pk):
    profile = get_profile()
    car = Car.objects.get(pk=pk)
    if request.method == 'GET':
        form = CarEditForm(instance=car)
    else:
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {'car': car, 'form': form, 'profile': profile}
    return render(request, template_name='car-edit.html', context=context)


def car_delete(request, pk):
    profile = get_profile()
    car = Car.objects.get(pk=pk)
    if request.method == 'GET':
        form = CarDeleteForm(instance=car)
    else:
        form = CarDeleteForm(request.POST, instance=car)
        form.save()
        return redirect('catalogue')

    context = {'form': form, 'car': car, 'profile': profile}

    return render(request, template_name='car-delete.html', context=context)
