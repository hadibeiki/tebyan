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
    eatekaf = Mregistereatekaf.objects.filter(contact__city=request.user.city)
    mosques = Mmosque.objects.filter(city=request.user.city)

    if request.method =="POST":
        update_request = request.POST.copy()
        update_request.update({'city': str(request.user.city.id)})
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
        form = registerForm(request.POST or None, request.FILES or None, instance=user)
        if form.is_valid():
                form.save()
                try:
                    selectuser = Mregistereatekaf.objects.get(contact__melicode=user.melicode)
                    url = reverse('gotogetway', kwargs={'id': selectuser.id, 'mosque':mosque.id})
                    return HttpResponseRedirect(url)
                except:
                    Mregistereatekaf.objects.create(
                        contact=user,
                        mosque=mosque,
                        payment="خیر",
                    )
                    url = reverse('gotogetway', kwargs={'id': user.id, 'mosque': mosque.id})
                    return HttpResponseRedirect(url)
    context = {
        'form':form
    }
    return render(request, "signup.html", context)


def go_to_gateway_view(request,id,mosque):
    selectRegister = Mregistereatekaf.objects.get(Q(contact_id=id) and Q(mosque_id=mosque))
    # خواندن مبلغ از هر جایی که مد نظر است
    amount = selectRegister.mosque.price
    # تنظیم شماره موبایل کاربر از هر جایی که مد نظر است
    user_mobile_number = str(selectRegister.contact.mobile)  # اختیاری

    factory = bankfactories.BankFactory()
    try:
        bank = factory.auto_create()  # or factory.create(bank_models.BankType.BMI) or set identifier
        bank.set_request(request)
        bank.set_amount(amount)
        # یو آر ال بازگشت به نرم افزار برای ادامه فرآیند
        bank.set_client_callback_url(reverse('callback-gateway', kwargs={'id': selectRegister.id}))
        bank.set_mobile_number(user_mobile_number)  # اختیاری

        # در صورت تمایل اتصال این رکورد به رکورد فاکتور یا هر چیزی که بعدا بتوانید ارتباط بین محصول یا خدمات را با این
        # پرداخت برقرار کنید.
        bank_record = bank.ready()

        # هدایت کاربر به درگاه بانک
        # return bank.redirect_gateway()
        context = bank.get_gateway()
        return render(request, 'redirect_to_bank.html', context=context)
    except AZBankGatewaysException as e:
        logging.critical(e)
        return render(request, 'redirect_to_bank.html')
        # raise e



def callback_gateway_view(request, id):
    selectregister = Mregistereatekaf.objects.get(id=id)
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
        selectregister.payment = "بله"
        selectmosque = Mmosque.objects.get(id=Mregistereatekaf.mosque.id)
        selectmosque.velocity = selectmosque.velocity-1
        selectmosque.save()
        selectregister.save()

        # پرداخت با موفقیت انجام پذیرفته است و بانک تایید کرده است.
        # می توانید کاربر را به صفحه نتیجه هدایت کنید یا نتیجه را نمایش دهید.
        messages.info(request, "با موفقیت انجام شد")
        return redirect("successPay", id=selectregister.id)
        # return HttpResponse("پرداخت با موفقیت انجام شد.")

    # پرداخت موفق نبوده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.
    selectregister.delete()
    return HttpResponse("پرداخت با شکست مواجه شده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.")


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


def successView(request, id):
    selectEatekaf = Mregistereatekaf.objects.get(id=id)
    contact ={
        "user":selectEatekaf
    }

    return render(request, "success.html", contact)