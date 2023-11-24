from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from petstagram_from_zero.common.forms import CommentAddForm
from petstagram_from_zero.pets.forms import PetBaseForm, PetEditForm, PetDeleteForm, PetAddForm
from petstagram_from_zero.pets.models import Pet


# PETS/VIEWS
@login_required
def pet_add(request):
    if request.method == 'GET':
        form = PetAddForm()
    else:
        form = PetAddForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()

            return redirect('profile details', pk=request.user.pk)

    context = {'form': form}
    return render(request, template_name='pets/pet-add-page.html', context=context)


def pet_details(request, username, pet_slug):
    pet = Pet.objects.filter(slug=pet_slug, user__username=username).first()
    all_photos = pet.photo_set.all()  # important!
    comment_form = CommentAddForm()

    context = {'pet': pet,
               'all_photos': all_photos,
               'username': username,
               'comment_form': comment_form,
               'is_owner': request.user == pet.user
               }
    return render(request, template_name='pets/pet-details-page.html', context=context)


def pet_edit(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug, user__username=username)
    if request.method == "GET":
        form = PetEditForm(instance=pet, )
    else:
        form = PetEditForm(request.POST, instance=pet, )
        if form.is_valid():
            form.save()
            return redirect('pet details', username=username, pet_slug=pet.slug)

    context = {'form': form, 'pet': pet, 'username': username}
    return render(request, template_name='pets/pet-edit-page.html', context=context)


def pet_delete(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug, user__username=username)

    if request.method == 'POST':
        pet.delete()
        return redirect('profile details', pk=1)

    form = PetDeleteForm(initial=pet.__dict__)
    context = {'form': form, 'username': username, 'pet_slug': pet_slug}
    return render(request, template_name='pets/pet-delete-page.html', context=context)
