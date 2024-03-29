"""taskmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from tasks.views import CreateTaskView, TaskDetailView, TaskUpdateView, TaskDeleteView, TaskListView
from user.views import UserSignupView, UserLoginView, user_logout

urlpatterns = [
    path('admin/', admin.site.urls),

    path('signup/', UserSignupView.as_view(), name='user_signup'),
    path('', UserLoginView.as_view(), name='user_login'),
    path('logout/', user_logout, name='user_logout'),

    path("home/", TaskListView.as_view(), name="home"),
    path('task/create/', CreateTaskView.as_view(), name='create_task'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='update_task'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='delete_task')

]
