from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from contact.forms import registerForm
from mosque.forms import mosqueForm
from gallery.forms import galleryForm
from mosque.models import Mmosque
from registerEatekaf.models import Mregistereatekaf


def admin2View(request, ):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('alldata', id=user.id)
        else:
            messages.info(request, "نام کاربری یا رمز عبور اشتباه است")
            return redirect('admin2')
    return render(request, "login.html", )

def admin3View(request, ):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('alldatamosque', id=user.id)
        else:
            messages.info(request, "نام کاربری یا رمز عبور اشتباه است")
            return redirect('admin3')


    return render(request, "login2.html",)


def Vindex(request, ):
    return render(request, "index.html", )


def Eatekafindex(request, ):
    mosques = Mmosque.objects.all()
    context = {
        'mosques': mosques
    }
    return render(request, "Eatekafindex.html", context)
