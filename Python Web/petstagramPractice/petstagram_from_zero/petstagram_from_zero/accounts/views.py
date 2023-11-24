from django.contrib.auth import views as auth_views, get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from petstagram_from_zero.accounts.forms import UserRegisterForm, UserEditForm

# ACCOUNTS/VIEWS
UserModel = get_user_model()


class UserSignIn(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    # next_page = reverse_lazy('home page')  Its setuped in the settings


class UserSignOut(auth_views.LogoutView):
    next_page = reverse_lazy('home page')


class UserSignUp(CreateView):
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('login')
    form_class = UserRegisterForm


class UserDetails(DetailView):
    context_object_name = 'profile'
    template_name = 'accounts/profile-details-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['likes_count'] = self.object.like_set.all().count()
        context['is_owner'] = self.request.user == self.object
        return context


class UserEdit(UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    form_class = UserEditForm
    model = UserModel

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.object.pk})


class UserDelete(DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('home page')
