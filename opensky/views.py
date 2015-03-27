from django.shortcuts import render
from django import forms
from opensky.models import CarouselImage, Feature, Equipment, Service, Worker, Partner
from django.core.mail import send_mail


class MyTextWidget(forms.TextInput):
    class Media:
        css = {'all': ('opensky/bootstrap/css/bootstrap.min.css', )}
        js = ('opensky/script/jquery-2.1.3.min.js',
              'opensky/bootstrap/js/bootstrap.min.js')


class MyTextareaWidget(forms.Textarea):
    class Media:
        css = {'all': ('opensky/bootstrap/css/bootstrap.min.css', )}
        js = ('opensky/script/jquery-2.1.3.min.js',
              'opensky/bootstrap/js/bootstrap.min.js')


class MyEmailWidget(forms.EmailInput):
    class Media:
        css = {'all': ('opensky/bootstrap/css/bootstrap.min.css', )}
        js = ('opensky/script/jquery-2.1.3.min.js',
              'opensky/bootstrap/js/bootstrap.min.js')


class SenderWidget(MyTextWidget):
    def __init__(self):
        self.attrs = {
            'placeholder': 'Ваше имя',
            'type': 'text',
            'class': 'form-control',
        }


class SubjWidget(MyTextWidget):
    def __init__(self):
        self.attrs = {
            'placeholder': 'Введите тему',
            'type': 'text',
            'class': 'form-control',
            }


class EmailWidget(MyEmailWidget):
    def __init__(self):
        self.attrs = {
            'placeholder': 'Ваш Email',
            'type': 'email',
            'class': 'form-control',
        }


class MessageWidget(MyTextareaWidget):
    def __init__(self):
        self.attrs = {
            'placeholder': 'Введите сообщение',
            'type':'text',
            'class': 'form-control',
        }


class MailForm(forms.Form):
    sender = forms.CharField(widget=SenderWidget, max_length=30)
    email = forms.EmailField(widget=EmailWidget)
    subj = forms.CharField(widget=SubjWidget, max_length=50)
    message = forms.CharField(widget=MessageWidget)


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
        'partners': Partner.objects.all(),
    }
    return render(request, 'opensky/company.html', data)


def workers(request):
    data = {
        'workers': Worker.objects.all(),
    }
    return render(request, 'opensky/workers.html', data)


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