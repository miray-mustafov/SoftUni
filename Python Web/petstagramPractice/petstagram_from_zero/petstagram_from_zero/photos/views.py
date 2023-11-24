from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from petstagram_from_zero.common.forms import CommentAddForm
from petstagram_from_zero.photos.forms import PhotoBaseForm, PhotoAddForm, PhotoEditForm
from petstagram_from_zero.photos.models import Photo


# PHOTOS / VIEWS


@login_required
def photo_add(request):
    if request.method == 'GET':
        form = PhotoAddForm()
    else:
        form = PhotoAddForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            form.save_m2m()

            return redirect('home page')

    context = {'form': form, }
    return render(request, template_name='photos/photo-add-page.html', context=context)

@login_required
def photo_details(request, pk):
    photo = Photo.objects.filter(pk=pk).first()
    likes = photo.like_set.all()
    comments = photo.comment_set.all()
    comment_form = CommentAddForm()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
        'comment_form': comment_form,
        'is_owner': photo.user == request.user
    }
    return render(request, template_name='photos/photo-details-page.html', context=context)


def photo_edit(request, pk):
    photo = Photo.objects.get(pk=pk)
    if request.method == "GET":
        form = PhotoEditForm(instance=photo, initial=photo.__dict__, )
    else:
        form = PhotoEditForm(request.POST, instance=photo, )
        if form.is_valid():
            form.save()
            return redirect('photo details', pk=pk)

    context = {
        'form': form,
    }
    return render(request, template_name='photos/photo-edit-page.html', context=context)


def photo_delete(request, pk):
    Photo.objects.get(pk=pk).delete()
    return redirect('home page')
