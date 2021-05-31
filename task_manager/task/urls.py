from django.urls import path
from .views import create_task_view, actual_tasks_view, edit_task, delete_task


urlpatterns = [
    path('', actual_tasks_view, name='actual_tasks'),
    path('form_task/', create_task_view, name='form_task'),
    path('edit/<int:pk>/', edit_task, name='edit'),
    path('delete_task/<int:pk>/', delete_task, name='delete')

]
