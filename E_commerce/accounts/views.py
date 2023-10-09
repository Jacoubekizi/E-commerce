from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from .forms import *
from django.contrib.auth import login,  logout, authenticate, update_session_auth_hash
from store.models import Customer, Order
# from django.contrib import messages

# from .backends import EmailBackend.authenticate

# Create your views here.

def sign_up(request):

    if request.user.is_authenticated:
        return redirect('store')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=True)
            customer = Customer.objects.create(
                 user = user,
                 name = user.username
            )

            order, created = Order.objects.get_or_create(
                 customer=customer,
                 complete = False
            )
            login(request, user)
            return redirect('store')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register/signup.html', {'form':form})



def ChangePassword(request):

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = FormChangePassword(request.user, request.POST)
            print(form.is_valid())
            if form.is_valid():
                form.save()
                return redirect ('store')
        else:
            form = FormChangePassword(request.user)
    context = {
        'form':form
    }
        
    return render(request, 'register/change_pass.html', context)
