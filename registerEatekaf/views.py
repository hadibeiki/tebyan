import datetime
import logging

import requests
from azbankgateways import bankfactories
from azbankgateways.exceptions import AZBankGatewaysException
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect
from azbankgateways import bankfactories, models as bank_models, default_settings as settings
# Create your views here.
from django.urls import reverse

from contact.forms import registerForm
from contact.models import Mcontact
from gallery.forms import galleryForm
from mosque.forms import mosqueForm
from mosque.models import Mmosque
from registerEatekaf.forms import registereatekafform
from registerEatekaf.models import Mregistereatekaf


def allData(request, id):
    mosqueform = mosqueForm()
    galleryform = galleryForm()
    galleryform.fields["mosqe"].queryset = Mmosque.objects.filter(city=request.user.city)
    eatekaf = Mregistereatekaf.objects.all()
    mosques = Mmosque.objects.all()

    if request.method =="POST":
        update_request = request.POST.copy()
        update_request.update({'city':request.user.city})
        addmosqueform = mosqueForm(update_request)
        if addmosqueform.is_valid():
            addmosqueform.save()
            messages.success(request, 'حله، ذخیره شد')
            return HttpResponseRedirect(reverse('alldata', kwargs={'id':request.user.id}))
    context = {
        'mosqueform': mosqueform,
        'eatekaf': eatekaf,
        'mosques': mosques,
        'galleryform':galleryform,
    }
    return render(request, "datacity.html", context)


def signupview(request):
    form = registerForm()
    if request.method == "POST":
        user = Mcontact.objects.get(melicode=request.POST['melicode'])
        mosque = Mmosque.objects.get(id=request.POST['mosque'])
        form = registerForm(request.POST)
        print("hadi")
        print(form.errors)
        if form.is_valid():
            try:
                registeruser = Mregistereatekaf.objects.get(Q(contact=user) & Q(mosque=mosque))
                if registeruser.pyorno == "بلی":
                    if registeruser.mosque.price >= mosque.price :
                        print("ali")
                        # go_to_gateway_view(request,mosque, user.mobile)
                    else:
                        messages.error(request, "شما قابلیت اینکار را ندارید")
                        return HttpResponseRedirect(reverse('signupurl'))
                else:
                    print("ali")
                    # go_to_gateway_view(request,mosque, user.mobile)
            except:
                Mregistereatekaf.objects.create(
                    contact=user,
                    mosque=mosque,
                    payment="خیر",
                )
                print("ahmad")
                # go_to_gateway_view(request,mosque, user.melicode)
            return redirect('index')
    context = {
        'form':form
    }
    return render(request, "signup.html", context)


def go_to_gateway_view(request,):
    # خواندن مبلغ از هر جایی که مد نظر است
    amount = 50000
    # تنظیم شماره موبایل کاربر از هر جایی که مد نظر است
    # user_mobile_number = str(mobile)  # اختیاری

    factory = bankfactories.BankFactory()
    try:
        bank = factory.auto_create()  # or factory.create(bank_models.BankType.BMI) or set identifier
        bank.set_request(request)
        bank.set_amount(amount)
        # یو آر ال بازگشت به نرم افزار برای ادامه فرآیند
        print("mobile")
        print("mosque")
        bank.set_client_callback_url(reverse('callback-gateway'))
        # bank.set_mobile_number(mobile)  # اختیاری

        # در صورت تمایل اتصال این رکورد به رکورد فاکتور یا هر چیزی که بعدا بتوانید ارتباط بین محصول یا خدمات را با این
        # پرداخت برقرار کنید.
        bank_record = bank.ready()

        # هدایت کاربر به درگاه بانک
        return bank.redirect_gateway()
    except AZBankGatewaysException as e:
        logging.critical(e)
        raise e



def callback_gateway_view(request,):

    tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
    if not tracking_code:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    try:
        bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
    except bank_models.Bank.DoesNotExist:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    # در این قسمت باید از طریق داده هایی که در بانک رکورد وجود دارد، رکورد متناظر یا هر اقدام مقتضی دیگر را انجام دهیم
    if bank_record.is_success:
        # پرداخت با موفقیت انجام پذیرفته است و بانک تایید کرده است.
        # می توانید کاربر را به صفحه نتیجه هدایت کنید یا نتیجه را نمایش دهید.
        # user = Mregistereatekaf.objects.get(Q(contact__mobile=mobile) and Q(mosque=mosque))
        # user.pyorno="بله"
        # user.save()
        messages.info(request, "با موفقیت انجام شد")
        return redirect("index",)

    # پرداخت موفق نبوده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.
    return HttpResponse(
        "پرداخت با شکست مواجه شده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.")


def reportview(request, id):
    mosques = Mmosque.objects.filter(city=request.user.city)
    allcitycontact = Mcontact.objects.filter(city=request.user.city)
    alonecontact = allcitycontact.filter(marital="مجرد")
    mariedcontact = allcitycontact.filter(marital="متاهل")
    underDiploma = allcitycontact.filter(education_id=1)
    diploma= allcitycontact.filter(education_id=2)
    bachler= allcitycontact.filter(education_id=3)
    master= allcitycontact.filter(education_id=4)
    doctor= allcitycontact.filter(education_id=5)
    age810= allcitycontact.filter(Q(age__lte=10) & Q(age__gte=8))
    age1015= allcitycontact.filter(Q(age__lte=15) & Q(age__gt=10))
    age1520= allcitycontact.filter(Q(age__lte=20) & Q(age__gt=15))
    age2030= allcitycontact.filter(Q(age__lte=30) & Q(age__gt=20))
    age3040= allcitycontact.filter(Q(age__lte=40) & Q(age__gt=30))
    age40inf= allcitycontact.filter(age__gt=40)


    context = {
        "mosques":mosques,
        "alonecontact":alonecontact,
        "mariedcontact":mariedcontact,
        'underDiploma':underDiploma,
        'diploma':diploma,
        'bachler':bachler,
        'master':master,
        'doctor':doctor,
        'age810':age810,
        'age1015':age1015,
        'age1520':age1520,
        'age2030':age2030,
        'age3040':age3040,
        'age40inf':age40inf,
    }
    return render(request, "chartdata.html", context)