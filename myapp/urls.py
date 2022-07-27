from django.urls import path
from.views import TaskList, TaskDetails

urlpatterns=[
    path('',home.as_view(), name='home'),
    path('', 'task-details/<int:pk>/', TaskDetails.as_view(), name='task_details'),
    path('', 'task-details/<int:pk>/', TaskDetails.as_view(), name='task_details'),

]