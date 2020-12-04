from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def add2(request):
    a = request.GET.get('a', 0)
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


def index(request):
    return render(request, 'home.html')


def add(request, a, b):
    c = int(a)+int(b)
    return HttpResponse(c)


def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('add', args=(a, b))
    )





