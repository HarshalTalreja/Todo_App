from django.urls import path
from task import views

urlpatterns = [
    path('', views.TaskList.as_view(), name='task_list_url'),
    path('<str:id>/completed/', views.TaskComplete.as_view(), name='task_complete_url'),
    path('<str:id>/delete/', views.TaskDelete.as_view(), name='task_delete_url'),
]
