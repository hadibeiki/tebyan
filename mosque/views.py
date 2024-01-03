from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from gallery.models import Mgallery
from mosque.models import Mmosque
from mosque.forms import mosqueForm


def selectMosque(request,):
    selectage = request.GET['age']
    if selectage =='':
        selectage = 0
    selectmosque = Mmosque.objects.filter(Q(sex_id=request.GET['sex']) & Q(city_id=request.GET['city']))
    context = {
        'mosques': selectmosque,
    }
    return render(request, "selectmosque.html", context)


def mosquedetail(request):
    mosquedata = request.GET['mosque']
    selectMosque = Mmosque.objects.get(id=mosquedata)
    galleries = Mgallery.objects.filter(mosqe=selectMosque)

    context = {
        'mosque':selectMosque,
        'galleries':galleries,
    }

    return render(request, "mosquedescription.html", context)

def mosquedit(request, id):
    selectMosque = Mmosque.objects.get(id=id)
    form = mosqueForm(instance=selectMosque)

    if request.method == "POST":
        form = mosqueForm(request.POST or None, instance=selectMosque)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.city = request.user.city
            obj.save()
            messages.success(request, "حله ذخیره شد")
            return redirect('alldata',id=request.user.id)

    context = {
        'item':selectMosque,
        'form':form,
    }

    return render(request, "mosqueedit.html", context)