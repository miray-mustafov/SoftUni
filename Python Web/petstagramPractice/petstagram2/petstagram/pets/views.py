from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet
from petstagram.common.forms import CommentForm


def details_pet(request, username, pet_slug):
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment_form = form.save(commit=False)

    context = {'comment_form': comment_form, }
    return render(request, template_name='pets/pet-details-page.html', context=context)


@login_required
def add_pet(request):
    if request.method == 'GET':
        form = PetCreateForm()
    else:  # request.method=='POST'
        form = PetCreateForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            return redirect('profile-details', pk=request.user.pk)

    context = {'form': form, }

    return render(request, template_name='pets/pet-add-page.html', context=context)


def edit_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'GET':
        form = PetEditForm(instance=pet, )
    else:  # request.method=='POST'
        form = PetEditForm(request.POST, instance=pet, )
        if form.is_valid():
            form.save()
            return redirect('details-pet', username, pet_slug)

    context = {'form': form, 'username': username, 'pet_slug': pet_slug, }

    return render(request, template_name='pets/pet-edit-page.html', context=context)


def delete_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)

    if request.method == 'POST':
        pet.delete()
        return redirect('profile-details', pk=request.user.pk)

    form = PetDeleteForm(initial=pet.__dict__)  # TO AUTOFILL THE FIELDS
    context = {'form': form, 'username': username, 'pet_slug': pet_slug, }
    return render(request, template_name='pets/pet-delete-page.html', context=context)
