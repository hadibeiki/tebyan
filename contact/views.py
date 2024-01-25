from datetime import datetime, timezone
from random import randint
from urllib.request import urlopen
from django.db.models import Q, Case, When
from django.core.exceptions import SuspiciousOperation
import requests
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from persiantools import digits

from ability.forms import abilityForm
from contact.forms import registerForm
from contact.models import Mcontact
from mosque.forms import mosqueForm
from mosque.models import Mmosque
from registerEatekaf.models import Mregistereatekaf


def viewindex(request):
    mosques = Mmosque.objects.all().order_by(Case(When(id=91, then=0), default=1))
    context = {
        'mosques': mosques
    }
    if request.method == 'POST':
        if "mobile" in request.POST:
            try:
                melicode = digits.fa_to_en(request.POST['melicode'])
                user = Mcontact.objects.get(melicode=melicode)
                try:
                    eatekafesh = Mregistereatekaf.objects.get(contact=user)
                    messages.error(request, "شما قبلا ثبت نام کرده اید.")
                    return HttpResponseRedirect(reverse('EatekafIndex'))
                except:
                    now = datetime.now(timezone.utc)
                    otp = rendomotp()
                    user.otp = otp
                    user.otpcreatedtime = now
                    user.save()
                    rest_test_send_sms(request.POST['mobile'], otp)
                    request.session['user-melicode'] = request.POST['melicode']
                    return HttpResponseRedirect(reverse('verify'))
            except:
                now = datetime.now(timezone.utc)
                otp = rendomotp()
                try:
                    Mcontact.objects.create(
                        name=" ",
                        family=" ",
                        dad=" ",
                        mobile=digits.fa_to_en(request.POST['mobile']),
                        melicode=digits.fa_to_en(request.POST['melicode']),
                        sex_id=3,
                        age=0,
                        price=0,
                        city_id=1,
                        education_id=1,
                        marital=1,
                        otp=otp,
                        otpcreatedtime=now,
                        testimonial=False,
                    )
                    rest_test_send_sms(request.POST['mobile'], otp)
                    request.session['user-melicode'] = request.POST['melicode']
                    return HttpResponseRedirect(reverse('verify'))
                except:
                    messages.error(request, "لطفا دوباره امتحان کنید")
                    return HttpResponseRedirect(reverse('EatekafIndex'))
    return render(request, "Eatekafindex.html", context)


def rendomotp():
    return randint(10000, 99999)


def rest_test_send_sms(mobile, otp):
    BaseAddress = "http://ippanel.com:8080/?apikey"
    apikey = '=SWtbyOMv1t0IaSLJDBFsykw10_go_7_oKlcw98l6vv0='
    pid = "&pid=psr8t6e408atkym"
    fnum = "&fnum=300070020000"
    tnum = "&tnum=" + str(mobile)
    p1 = "&p1=otp"
    v1 = "&v1=" + str(otp)
    url = BaseAddress + apikey + pid + fnum + tnum + p1 + v1
    x = urlopen(str(url), )
    return HttpResponse(x.read())


# def Vverify(request,):
#     return render(request, "verify.html",)


def Vverify(request):
    try:
        melicode = digits.fa_to_en(request.session.get('user-melicode'))
        user = Mcontact.objects.get(melicode=melicode)
        if request.method == "POST":
            if not checkOtpExp(user.mobile, user.melicode):
                messages.error(request, "کد اعتبار سنجی منقضی شده است")
                return HttpResponseRedirect(reverse('EatekafIndex'))
            if user.otp != request.POST['otp']:
                messages.error(request, "کد اعتبار سنجی صحیح نیست")
                return HttpResponseRedirect(reverse('verify'))
            return HttpResponseRedirect(reverse('urladdcontact',kwargs={'melicode': user.melicode}))
        return render(request, 'verify.html')
    except:
        messages.error(request, "کاربر با این مشخصات موجود نیست")
        return HttpResponseRedirect(reverse('EatekafIndex'))


def checkOtpExp(mobile,melicode):
    try:
        user = Mcontact.objects.get(mobile=mobile, melicode=melicode)
        now = datetime.now(timezone.utc)
        otp_time = user.otpcreatedtime
        difftime = now - otp_time
        if difftime.seconds > 120:
            return False
        return True
    except:
        return False


def viewaddcontact(request,melicode):
    selectcontact = Mcontact.objects.get(melicode=melicode)
    # mosques = Mmosque.objects.filter(city=1)

    form = registerForm(instance=selectcontact)
    abilityform = abilityForm()
    context = {
        'form': form,
        # 'mosques':mosques,
        'abilityForm': abilityform,
    }
    return render(request, "signup.html", context)


def deletecontact(request,melicode):
    Mregistereatekaf.objects.get(contact__melicode=melicode).delete()
    messages.success(request, "کاربر حذف شد")
    return redirect('alldata',id=request.user.id)


def confirmcontact(request,melicode):
    selectEatekaf = Mregistereatekaf.objects.get(contact__melicode=melicode)
    selectEatekaf.payment = "بله"
    selectEatekaf.save()
    messages.success(request, "کاربر تایید شد")
    return redirect('alldatamosque',id=request.user.id)