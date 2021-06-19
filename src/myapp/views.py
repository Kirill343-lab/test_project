from django.shortcuts import render
from .models import Vacancy
from .forms import FindForm

def home_view(request):
    form = FindForm()
    language=request.GET.get("language")
    city=request.GET.get("city")
    form_request = dict()
    if language or city:
        if language:
            form_request['language__slug'] = language
        if city:
            form_request['city__slug'] = city

    querySet = Vacancy.objects.filter(**form_request)
    return render(request, 'myapp/home.html', {'object_list': querySet,
                                                      'form': form})


# Create your views here.
