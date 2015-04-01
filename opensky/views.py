from django.shortcuts import render
from django import forms
from opensky.models import *
from django.core import mail
from django.http import HttpResponse
from django.core.mail.backends.smtp import EmailBackend

#Not use
class MyStyle(forms.Widget):
    class Media:
        css = {'all': ('opensky/bootstrap/css/bootstrap.min.css', )}
        js = ('opensky/script/jquery-2.1.3.min.js',
              'opensky/bootstrap/js/bootstrap.min.js')


class SenderWidget(forms.TextInput):
    def __init__(self):
        self.attrs = {
            'placeholder': 'Ваше имя',
            'type': 'text',
            'class': 'form-control',
        }


class SubjWidget(forms.TextInput):
    def __init__(self):
        self.attrs = {
            'placeholder': 'Введите тему',
            'type': 'text',
            'class': 'form-control',
            }


class EmailWidget(forms.EmailInput):
    def __init__(self):
        self.attrs = {
            'placeholder': 'Ваш Email',
            'type': 'email',
            'class': 'form-control',
        }


class MessageWidget(forms.Textarea):
    def __init__(self):
        self.attrs = {
            'placeholder': 'Введите сообщение',
            'type':'text',
            'class': 'form-control',
        }


class MailForm(forms.Form):
    sender = forms.CharField(widget=SenderWidget, max_length=30)
    email = forms.EmailField(widget=EmailWidget, max_length=30)
    subj = forms.CharField(widget=SubjWidget, max_length=50)
    message = forms.CharField(widget=MessageWidget, max_length=500)


def index(request):
    data = {
        'carousel_images': CarouselImage.objects.all(),
        'widgets': SocialWidget.objects.all(),
        'office': Office.objects.get(pk=1),
    }
    return render(request, 'opensky/index.html', data)


def equipment(request):
    data = {
        'equipments': Equipment.objects.all(),
        'widgets': SocialWidget.objects.all(),
        'office': Office.objects.get(pk=1),
    }
    return render(request, 'opensky/equipment.html', data)


def features(request):
    data = {
        'features': Feature.objects.all(),
        'widgets': SocialWidget.objects.all(),
        'office': Office.objects.get(pk=1),
    }
    return render(request, 'opensky/features.html', data)


def pricing(request):
    data = {
        'prices': Price.objects.all(),
        'widgets': SocialWidget.objects.all(),
        'office': Office.objects.get(pk=1),
    }
    return render(request, 'opensky/pricing.html', data)


def services(request):
    data = {
        'services': Service.objects.all(),
        'widgets': SocialWidget.objects.all(),
        'office': Office.objects.get(pk=1),
    }
    return render(request, 'opensky/services.html', data)


def company(request):
    data = {
        'partners': Partner.objects.all(),
        'widgets': SocialWidget.objects.all(),
        'office': Office.objects.get(pk=1),
        'about_company': Blog.objects.get(mark="about_company"),
    }
    return render(request, 'opensky/company.html', data)


def workers(request):
    data = {
        'workers': Worker.objects.all(),
        'widgets': SocialWidget.objects.all(),
        'office': Office.objects.get(pk=1),
    }
    return render(request, 'opensky/workers.html', data)


def contacts(request):
    office = Office.objects.get(pk=1)
    office_mail = office.email
    server_mail = 'ooo.service-partner@yandex.ru'
    data = {
        'office': office,
        'widgets': SocialWidget.objects.all(),
    }
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            sender = form.cleaned_data['sender']
            email = form.cleaned_data['email']
            subj = form.cleaned_data['subj']
            message = form.cleaned_data['message']
            s = ":".join([sender, email, subj])
            mail.send_mail(s, message, server_mail, [office_mail], fail_silently=False)
            data['form'] = form
            data['thank'] = True
            return render(request, 'opensky/contacts.html', data)
    else:
        data['form'] = MailForm()
        data['thank'] = False
    return render(request, 'opensky/contacts.html', data)