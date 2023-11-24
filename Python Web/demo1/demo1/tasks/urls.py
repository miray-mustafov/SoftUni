# demo1.tasks.urls

from django.urls import path
from demo1.tasks.views import bare_minimum_view, show_all_tasks, index

urlpatterns = (
    #http://localhost:8000/tasks/
    path('', index),
    #http://localhost:8000/tasks/it-works/
    path('it-works/', bare_minimum_view),
    #достъпно на http://localhost:8000/tasks/all
    path('all/', show_all_tasks),
    path('mall/', index),

    # localhost:8000/tasks/create
    #path('create/', create),
)