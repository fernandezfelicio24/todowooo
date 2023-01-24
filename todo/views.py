from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login

# Create your views here.
def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error':'That username has already been taken. Please choose a new  username'})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currentodos')
            except IntegrityError:

                return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': 'The username has already been taken. Please choose a new username'})

        else:
            return render(request, 'todo/signupuser.html', {'form':UserCreationForm(), 'error':'Password did not match'})
            # Tell the user the password didn't match


def currentodos(request):
    return render(request, 'todo/curentodos.html')