from django import http
from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from petstagram.common.forms import CommentForm, SearchForm
from petstagram.common.models import Like
from petstagram.photos.models import Photo


def apply_user_liked_photo(photo):
    # TODO: Fix this for current user when authentication available
    photo.is_liked_by_user = photo.like_set.all()
    return photo


def show_home_page(request):
    photos = Photo.objects.all()
    all_photos = [apply_user_liked_photo(photo) for photo in photos]
    photo1 = all_photos[0]
    # print(all_photos)

    search_form = SearchForm()
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            all_photos = photos.filter(tagged_pets__name__icontains=search_form.cleaned_data['pet_name'])

    comment_form = CommentForm()
    context = {
        'all_photos': all_photos,
        'comment_form': comment_form,
        'search_form': search_form,
    }

    return render(request, template_name='common/home-page.html', context=context)


def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    # print(photo)
    liked_object = Like.objects.filter(to_photo_id=photo_id).first()
    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo=photo)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def copy_link_to_clipboard(request, photo_id):
    copy(request.META['HTTP_HOST'] + resolve_url('details-photo', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def add_comment(request, photo_id):
    if request.method == 'POST':
        photo = Photo.objects.get(id=photo_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.save()

    return redirect('home-page')
    # return redirect(request.META['HTTP_PREFERER']+f'#{photo_id}')
