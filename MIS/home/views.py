from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import *

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('counselorhome')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            user1 = LoginUser.objects.get(user = user)
            
            if user is not None:
                # user1 = LoginUser.objects.get(user = user)
                # print('User1 : ', user1.role)
                login(request,user)
                if user1.role == 'counselor':
                    print("Logged In as Counselor")
                    return redirect('counselorhome')
                elif user1.role == 'trainer':
                    print("Logged In as Trainer")
                    return redirect('trainerhome')
            else:
                messages.info(request, 'Username  OR Password is incorrect. ')
                # return render(request,'index.html')
                
        else:
            return render(request,'index.html')

def logout_view(request):
    logout(request)
    return redirect('login')

    # if request.user.is_authenticated:
    #     user = request.user
    #     candidate = LoginUser.objects.get(user = user)
    #     context = {'candidate' : candidate}
    #     return render(request, 'counselorhome.html')
    # else:
    #     return render(request,'index.html')

