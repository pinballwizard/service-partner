from django.shortcuts import render
from django import forms
from opensky.models import CarouselImage, Feature, Equipment, Service
from django.core.mail import send_mail


class MailForm(forms.Form):
    sender = forms.CharField(label='', max_length=30)
    email = forms.EmailField(label='', error_messages={'required': "Пожалуйста введите свой e-mail"})
    subj = forms.CharField(label='', max_length=50)
    message = forms.CharField(label='')


def index(request):
    data = {
        'carousel_images': CarouselImage.objects.all(),
    }
    return render(request, 'opensky/index.html', data)


def equipment(request):
    data = {
        'equipments': Equipment.objects.all(),
    }
    return render(request, 'opensky/equipment.html', data)


def features(request):
    data = {
        'features': Feature.objects.all(),
    }
    return render(request, 'opensky/features.html', data)


def pricing(request):
    data = {
        'features': Feature.objects.all(),
    }
    return render(request, 'opensky/pricing.html', data)


def services(request):
    data = {
        'services': Service.objects.all(),
    }
    return render(request, 'opensky/services.html', data)


def company(request):
    data = {
        'services': Service.objects.all(),
    }
    return render(request, 'opensky/company.html', data)


def contacts(request):
    office_mail = 'menstenebris@gmail.com'
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            sender = form.cleaned_data['sender']
            email = form.cleaned_data['email']
            subj = form.cleaned_data['subj']
            message = form.cleaned_data['message']
            s = sender+": "+subj
            send_mail(s, message, email, [office_mail], fail_silently=False)
            data = {'sender': sender}
            return render(request, 'opensky/thank.html', data)
    else:
        form = MailForm()
    data = {
        'form': form,
    }
    return render(request, 'opensky/contacts.html', data)