from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
# Create your views here.
from gallery.forms import galleryForm
from gallery.models import Mgallery


def selectgallery(request, id):
    galleries = Mgallery.objects.filter(mosqe_id=id)
    context = {
        'galleries':galleries
    }
    return render(request, "signup.html", context)

def addgallery(request):
    if request.method =="POST":
        form = galleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'حله، ذخیره شد')
            return HttpResponseRedirect(reverse('alldata', kwargs={'id':request.user.id}))
