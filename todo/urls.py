from django.urls import path
from . import views


urlpatterns = [
    # Mark as add task
    path('addtask/', views.addTask, name='addTask'),

    # Mark as done task
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    
    # Mark as undone task
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),

    # Mark as edit task
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),

    # Mark as delete task
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),

]