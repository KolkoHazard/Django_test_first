from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse

# Create your views here.
def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account is not active")
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password{}".format(username,password))
            return HttpResponse("invalid login details supplied")
    else:
        return render(request,'user_login/user_login.html',{})
