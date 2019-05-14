from django.urls import path
from api import views

urlpatterns = [
    path('tasklists/',views.TasklistList.as_view()),
    path('tasklists/<int:pk>/', views.TasklistDetail.as_view()),
    path('tasklists/<int:pk>/tasks/', views.TaskListTasks.as_view()),

    path('users/', views.UserList.as_view()),
    path('login/', views.login),
    path('logout/', views.logout),

]