from django.contrib.auth import views as auth_views, get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from petstagram.accounts.forms import PetstagramUserCreationForm, LoginForm, PetstagramUserEditForm

UserModel = get_user_model()


class UserRegisterView(views.CreateView):
    # model = UserModel
    form_class = PetstagramUserCreationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('login')


class UserLoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login-page.html'
    next_page = reverse_lazy('home-page')


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('login')


class UserEditView(views.UpdateView):
    model = UserModel
    form_class = PetstagramUserEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})


class UserDetailsView(views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object
        context['pets_count'] = self.object.pet_set.count()

        # photos = self.object.photo_set \
        #     .prefetch_related('photo_set')
        #
        # context['photos_count'] = photos.count()
        # context['likes_count'] = sum(x.like_set.count() for x in photos)

        return context


class UserDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('home-page')


# #
# # def login(request):
# #     return render(request, template_name='accounts/login-page.html')
# #
# # function based views
# # def register(request):
# #     return render(request, template_name='accounts/register-page.html')
# #
# #
# # def show_profile_details(request, pk):  # ?????? v setupa ne e s pk
# #     return render(request, template_name='accounts/profile-details-page.html')
#
#
# def edit_profile(request, pk):
#     return render(request, template_name='accounts/profile-edit-page.html')
