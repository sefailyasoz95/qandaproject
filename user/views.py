from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

from user.models import SignUpForm

def profile(request):
    current_user = request.user
    profile = User.objects.get(id=current_user.id)
    context = {
        'profile': profile
    }
    return render(request,'user/profile.html',context)

def logout_user(request):
    logout(request)
    return redirect('account/login')

def signup_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created, you can now Login!")
            return HttpResponseRedirect("/accounts/login")
        else:
            messages.warning(request, "There was an error in your form, please try again.")
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
