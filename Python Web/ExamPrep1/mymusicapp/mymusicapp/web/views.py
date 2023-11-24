from django.shortcuts import render, redirect

from mymusicapp.web.forms import CreateProfileForm, CreateAlbumForm, EditAlbumForm, DeleteAlbumForm, DeleteProfileForm
from mymusicapp.web.models import Profile, Album


def home_page_view(request):
    # If there is no profile
    profile = Profile.objects.all()
    if not profile:
        if request.method == 'GET':
            form = CreateProfileForm()
        else:  # POST
            form = CreateProfileForm(request.POST)
            if form.is_valid():
                form.save()
                # context = {'form': form, 'profile': profile, }
                return redirect('home-page')

        context = {'form': form, 'profile': profile, 'hide_some_links': True}
        return render(request, template_name='home-no-profile.html', context=context)

    else:
        context = {
            'albums': Album.objects.all()
        }
        return render(request, template_name='home-with-profile.html', context=context)


def profile_details_view(request):
    profile = Profile.objects.all()[0]
    albums_count = Album.objects.all().count()
    context = {'profile': profile, 'albums_count': albums_count}
    return render(request, template_name='profile-details.html', context=context)


def profile_delete_view(request):
    profile = Profile.objects.all()[0]
    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        # if_form is valid?
        form.save()
        return redirect('home-page')

    context = {'form': form}
    return render(request, template_name='profile-delete.html', context=context)


def album_add_view(request):
    form = CreateAlbumForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home-page')

    context = {'form': form}
    return render(request, template_name='add-album.html', context=context)


def album_details_view(request, pk):
    album = Album.objects.filter(pk=pk).get()
    context = {'album': album, }

    return render(request, template_name='album-details.html', context=context)


def album_edit_view(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'GET':
        form = EditAlbumForm(instance=album)
    else:
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {'form': form, 'album': album, }
    return render(request, template_name='edit-album.html', context=context)


def album_delete_view(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'GET':
        form = DeleteAlbumForm(instance=album)
    else:
        # Album.objects.filter(pk=pk).get().delete() Do NOT do this!
        form = DeleteAlbumForm(request.POST, instance=album)
        form.save()  # album.delete()
        return redirect('home-page')

    context = {'form': form, 'album': album, }
    return render(request, template_name='delete-album.html', context=context)
