from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.forms.models import model_to_dict
from mezzanine.conf import settings


# Create your views here.

def instrument_list(request):
    return render(request, 'instrument/instrument-list.html')
