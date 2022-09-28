from django.urls import path
from todolist.views import show_todolist
from todolist.views import register
from todolist.views import login_user #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import logout_user #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import create_new_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'), #sesuaikan dengan nama fungsi yang dibuat
    path('login/', login_user, name='login_user'), #sesuaikan dengan nama fungsi yang dibuat
    path('logout/', logout_user, name='logout_user'),
    path('create-task/', create_new_task, name='create_new_task'),
]