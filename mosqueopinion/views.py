from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from mosqueopinion.forms import mosqueOpiniojnForm


def mosqueOpinion(request,):
    form = mosqueOpiniojnForm()
    if request.method == "POST":
        form = mosqueOpiniojnForm(request.POST or None)
        if form.is_valid:
            form.save()
            messages.success(request,'باتشکر از کمک شما ')
            return render(request,'Eatekafindex.html',)
    context = {
        'form': form,
    }

    return render(request, 'mosqueopinion.html', context)