from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from todolist.forms import CreateTaskForm
from todolist.models import Task
import datetime
from django.http import HttpResponseRedirect , HttpResponseNotFound , HttpResponse
from django.urls import reverse
from django.core import serializers

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.filter(user=request.user) # filter buat nampilin task sesuai dngn yg log in
    context = {
        'list_data': data_todolist,
        'username': request.user.get_username(),
        
    }
    return render(request, "todolist.html",context)



def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login_user')
    
    context = {'form':form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login_user'))
    response.delete_cookie('last_login')
    return response

#membuat task baru
def create_new_task(request):
    form = CreateTaskForm() #membuat objek form baru

    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid(): # buat check inputan user sdh valid / ga
            new_task = Task() # buat objek task baru
            new_task.user = request.user # buat ngisi atribut dr task baru
            new_task.date = datetime.datetime.now()
            new_task.title = form.cleaned_data['judul_task']
            new_task.description = form.cleaned_data['deskripsi_task']
            new_task.save()
            messages.success(request, 'Data telah berhasil dibuat!')
            return redirect('todolist:show_todolist')

    
    context = {'form':form} #gunanya masukin form ke dalam template
    return render(request, 'createtask.html', context)


def delete_task(request, id):
    data_task = Task.objects.get(id=id)
    data_task.delete()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))


@login_required(login_url='/todolist/login/')
def todolist_json(request):
    data_task = Task.objects.all().filter(usernames=request.user)
    return HttpResponse(serializers.serialize('json', data_task), content_type="application/json")

@login_required(login_url='/todolist/login/')
def todolist_add(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")

        task = Task.objects.create(title=title, description=description, date=datetime.date.today(), usernames=request.user)
        task.save()
        result = {
            'fields':{
                'title': task.title,
                'description': task.description,
                'date': task.date,
            },
            'pk': task.pk
        }

        return HttpResponse(b"CREATED", status=200)

    return HttpResponseNotFound()