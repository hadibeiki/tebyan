from datetime import datetime, timezone
from random import randint
from urllib.request import urlopen
from django.db.models import Q
from django.core.exceptions import SuspiciousOperation
import requests
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from contact.forms import registerForm
from contact.models import Mcontact
from mosque.forms import mosqueForm
from mosque.models import Mmosque
from registerEatekaf.models import Mregistereatekaf


def viewindex(request, ):
    if request.method == 'POST':
        if "mobile" in request.POST:
            try:
                mobile = request.POST['mobile']
                melicode = request.POST['melicode']
                user = Mcontact.objects.get(mobile=mobile,melicode=melicode)
                now = datetime.now(timezone.utc)
                otp_time = user.otpcreatedtime
                difftime = now - otp_time
                if difftime.seconds > 120:
                    otp = rendomotp()
                    # rest_test_send_sms(mobile, otp)
                    user.otp = otp
                    user.otpcreatedtime = datetime.now(timezone.utc)
                    user.save()
                    request.session['user-mobile'] = user.mobile
                    request.session['user-melicode'] = user.melicode
                    return HttpResponseRedirect(reverse('verify'))
                else:
                    messages.error(request, "کد تایید قبلا برای شما ارسال شده است")
                    return HttpResponseRedirect(reverse('verify'))
            except:
                now = datetime.now(timezone.utc)
                otp = rendomotp()
                try:
                    Mcontact.objects.create(
                        name=" ",
                        family=" ",
                        dad=" ",
                        mobile=request.POST['mobile'],
                        melicode=request.POST['melicode'],
                        sex_id=1,
                        age=0,
                        price=0,
                        city_id=1,
                        education_id=1,
                        marital=1,
                        otp=otp,
                        otpcreatedtime=now,
                    )
                    # rest_test_send_sms(request.POST['mobile'], otp)
                    request.session['user-mobile'] = request.POST['mobile']
                    request.session['user-melicode'] = request.POST['melicode']
                    return HttpResponseRedirect(reverse('verify'))
                except:
                    messages.error(request, "این کد ملی ثبت شده است لطفا با همان موبایل قبلی ثبت نام کنید")
                    return HttpResponseRedirect(reverse('index'))


    return render(request, "index.html")


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
        mobile = request.session.get('user-mobile')
        melicode = request.session.get('user-melicode')
        user = Mcontact.objects.get(mobile=mobile, melicode=melicode)
        if request.method == "POST":
            if not checkOtpExp(user.mobile, user.melicode):
                messages.error(request, "کد اعتبار سنجی منقضی شده است")
                return HttpResponseRedirect(reverse('index'))
            if user.otp != request.POST['otp']:
                messages.error(request, "کد اعتبار سنجی صحیح نیست")
                return HttpResponseRedirect(reverse('verify'))
            return HttpResponseRedirect(reverse('urladdoreditcontact',kwargs={'melicode': user.melicode}))
        return render(request, 'verify.html')
    except:
        messages.error(request, "کاربر با این مشخصات موجود نیست")
        return HttpResponseRedirect(reverse('index'))


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


def viewaddoreditcontact(request,melicode):
    selectcontact = Mcontact.objects.get(melicode=melicode)
    try:
        registeruser = Mregistereatekaf.objects.get(contact=selectcontact)
        mosques = Mmosque.objects.filter(id=registeruser.mosque.id)
    except:
        mosques = Mmosque.objects.filter(city=1)

    form = registerForm(instance=selectcontact)
    context = {
        'form': form,
        'mosques':mosques
    }
    return render(request, "signup.html", context)
