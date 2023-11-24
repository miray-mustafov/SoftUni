from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from petstagram_from_zero.common.forms import CommentAddForm, SearchForm
from petstagram_from_zero.common.models import Like, Comment
from petstagram_from_zero.photos.models import Photo


# Create your views here.
def home_page(request):
    all_photos = Photo.objects.all()
    comment_form = CommentAddForm()
    if request.user.is_authenticated:
        all_liked_photo_by_request_user = [like.to_photo_id for like in request.user.like_set.all()]
    else:
        all_liked_photo_by_request_user = []

    search_form = SearchForm()
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            all_photos = all_photos.filter(tagged_pets__name__icontains=search_form.cleaned_data['pet_name'])

    context = {
        'all_photos': all_photos,
        'comment_form': comment_form,
        'search_form': search_form,
        'all_liked_photo_by_request_user': all_liked_photo_by_request_user,
    }
    return render(request, template_name='common/home-page.html', context=context)


@login_required
def like_functionality(request, photo_pk):
    liked_photo = Like.objects.filter(to_photo_id=photo_pk, user=request.user).first()

    if liked_photo:
        liked_photo.delete()
    else:
        current_like = Like.objects.create(
            to_photo_id=photo_pk,
            user=request.user
        )

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_pk}')


def share_functionality(request, photo_pk):  # for now just copies link to clipboard
    copy(request.META['HTTP_HOST'] + resolve_url('photo details', photo_pk))
    return redirect(request.META['HTTP_REFERER'] + f'#{photo_pk}')


@login_required
def comment_functionality(request, photo_pk):
    comment_form = CommentAddForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)  # Does not persist to DB
        comment.to_photo_id = photo_pk
        comment.user = request.user
        comment.save()

        return redirect(request.META['HTTP_REFERER'] + f'#{photo_pk}')
    return Exception('Comment_form not valid in common.views.comment_functionality')
    # Comment.objects.create(to_photo_id=photo_pk)
