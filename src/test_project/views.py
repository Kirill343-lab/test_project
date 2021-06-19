from django.shortcuts import render
import datetime
from .models import Vacancy

def home_view(request):
    querySet = Vacancy.objects.all()
    return render(request, 'base.html', {'object_list': querySet})


def home (request):
    date = datetime.datetime.now().date()
    name = 'Kirill'
    received_info ={'name': name, 'date': date}
    return render(request, 'base.html', received_info)
