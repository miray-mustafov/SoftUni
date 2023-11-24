from django.urls import path
from django.views.generic import DetailView

from CBViews_demo.web.views import home_page_view, register_page_view, HomeView, HomeView2, IndexView, \
    IndexWithTemplateView, EmployeeDetailsView, EmployeeCreateView

urlpatterns = (
    # path('', home_page_view, name='home-page'),
    # path('', IndexView.as_view()),
    path('', IndexWithTemplateView.as_view(), name='home-page'),
    path('register/', register_page_view, name='register-page'),
    path('details/<int:pk>/', EmployeeDetailsView.as_view(), name='details-page'),
    path('create/', EmployeeCreateView.as_view(), name='create-page'),
    path('1/', HomeView.get_view()),
    path('2/', HomeView2.get_view()),
)
