# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect


def main(request):
    return render(request, 'main.html')


def register(request):
    errors = {}
    if request.method == "POST":
        errors = User.validate(request.POST)
        for key, value in errors.iteritems():
            messages.error(request, '{}: {}'.format(key, value))
    if errors == {}:
        password = bcrypt.hashpw(
            request.POST['password'].encode(), bcrypt.gensalt(5))
        try:
            User.objects.create(first_name=request.POST['first_name'],
                                last_name=request.POST['last_name'],
                                email=request.POST['email'],
                                password=password)
            request.session['email'] = request.POST['email']
            return redirect("/success")
        except:
            # handle unique constraint gracefully
            messages.error(request, "This email already exists")

    return redirect("/")


def login(request):
    email = request.POST['email']
    password = (request.POST['password'])
    try:
        user = User.objects.get(email=email)
    except:
        messages.error(request, "email could not be found")
        return redirect("/")

    if bcrypt.checkpw(password.encode(), user.password.encode()):
        request.session['email'] = request.POST['email']
        return redirect("/quotes")
    else:
        messages.error(request, "your password did not match!")
        return redirect("/")


def logout(request):
    try:
        del request.session['email']
    except:
        pass
    return redirect("/")


def success(request):
    context = {
        'first_name': User.objects.get(email=request.session['email']).first_name
    }
    return render(request, 'quotes.html', context)


def userscount(request):
    context = {
        'first_name': User.objects.get(email=request.session['email']).first_name
    }
        return render(request, 'userscount.html', context)
