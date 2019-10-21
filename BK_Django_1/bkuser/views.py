# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password

from .models import Bkuser
from .forms import LoginForm

# Create your views here.

def home(request):
    # user_id = request.session.get('user')
    #
    # if user_id:
    #     bkuser = Bkuser.objects.get(pk=user_id)
    #############################################
    # Transfer Session Process to Home.html instead.

    return render(request, 'home.html', )

def login(request):
    ##########################################
    ##############USING FORM.PY###############
    ##########################################
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            #session
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form':form})
    ##########################################
    ##########################################
    ##########################################
    
    # if request.method == 'GET':
    #     return render(request, 'login.html')
    # elif request.method == 'POST':
    #     username = request.POST.get('username', None)
    #     password = request.POST.get('password', None)
    #
    #     res_data = {}
    #
    #     if not (username and password):
    #         res_data['error'] = 'Insert all data'
    #     else:
    #         bkuser = Bkuser.objects.get(username=username)
    #         if check_password(password, bkuser.password):
    #             # Login Process, Matching Password
    #             # Session Start(save)
    #             request.session['user'] = bkuser.id
    #             # Redirect
    #             # return redirect('http://www.google.com')
    #             return redirect('/') #Home
    #
    #             pass
    #         else:
    #             res_data['error'] = 'Password is incorrect'
    #
    #     return render(request, 'login.html', res_data)

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')

def register(request):
    # function name should be html file
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['useremail']
        re_password = request.POST['re-password']

        res_data = {}
        
        if not (username and password and re_password):
            res_data['error'] = 'Insert all data'
        
        if password != re_password:
            res_data['error'] = 'Password does not match'

        bkuser = Bkuser(
            username = username,
            password = make_password(password),
            useremail = email
        )

        bkuser.save()

        return render(request, 'register.html', res_data)