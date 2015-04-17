from django.shortcuts import render
from django import forms
from opensky.models import *
from django.core import mail
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _


class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ['sender', 'email', 'subject', 'message']
        error_messages = {
            'sender': {
                'blank': _("Заполните поле"),
            },
        }
        localized_fields = ('__all__',)
        widgets = {
            'sender': forms.TextInput(attrs={
                'placeholder': 'Ваше имя',
                'type': 'text',
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Ваш Email',
                'type': 'email',
                'class': 'form-control',
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Введите тему',
                'type': 'text',
                'class': 'form-control',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Введите сообщение',
                'type':'text',
                'class': 'form-control',
                'rows': 5,
            }),
        }


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
        'form': MailForm(),
        'thank': False,
    }
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            sender = form.cleaned_data['sender']
            email = form.cleaned_data['email']
            subj = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            s = ":".join([sender, email, subj])
            mail.send_mail(s, message, server_mail, [office_mail], fail_silently=False)
            data['form'] = form
            data['thank'] = True
            form.save()
        else:
            data['form'] = form
    return render(request, 'opensky/contacts.html', data)