from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from .forms import UserRegistrationForm

# Create your models here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You can log in now.')
            return redirect('auth-login')
    else:
        form = UserRegistrationForm()
    return render(request,'accounts/register.html', {'form': form})

@login_required
def user_profile(request):
    return render(request, 'accounts/profile.html')