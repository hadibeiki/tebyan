from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from gallery.models import Mgallery
from mosque.models import Mmosque
from mosque.forms import mosqueForm
from geopy.geocoders import Nominatim
import folium


def selectMosque(request,):
    selectage = request.GET['age']
    if selectage =='':
        selectage = 0
    selectmosque = Mmosque.objects.filter(Q(sex_id=request.GET['sex']) & Q(city_id=request.GET['city']) & Q(endage__gt=selectage) & Q(startage__lte=selectage) & Q(velocity__gt=0))
    context = {
        'mosques': selectmosque,
    }
    return render(request, "selectmosque.html", context)


def mosquedetail(request):
    mosquedata = request.GET['mosque']
    selectMosque = Mmosque.objects.get(id=mosquedata)
    galleries = Mgallery.objects.filter(mosqe=selectMosque)

    geolocattion = Nominatim(user_agent='measurements')
    # kashan = geolocattion.geocode("kashan")
    # d_late = selectMosque.latitude
    # d_long = selectMosque.longitude
    pointA = (selectMosque.latitude, selectMosque.longtude)
    m = folium.Map(width=1500, height=400, location=pointA)
    m.fit_bounds([[30.058100, 57.347689],[32.832000, 52.774325]])
    folium.Marker([selectMosque.latitude, selectMosque.longtude], tooltip=str(selectMosque.name), popup=str(selectMosque.name), icon=folium.Icon(color='purple')).add_to(m)
    m = m._repr_html_()

    context = {
        'map':m,
        'mosque':selectMosque,
        'galleries':galleries,
    }

    return render(request, "mosquedescription.html", context)

def mosquedit(request, id):
    selectMosque = Mmosque.objects.get(id=id)
    form = mosqueForm(instance=selectMosque)

    if request.method == "POST":
        update_request = request.POST.copy()
        update_request.update({'city': str(request.user.city.id)})
        form = mosqueForm(update_request or None, instance=selectMosque)
        if form.is_valid():
            form.save()
            messages.success(request, "حله ذخیره شد")
            return redirect('alldata',id=request.user.id)

    context = {
        'item':selectMosque,
        'form':form,
    }

    return render(request, "mosqueedit.html", context)

