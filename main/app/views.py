from django.shortcuts import render
from django.http import HttpResponse
from .models import Board

# Create your views here.


def index(request):
    boards = Board.objects.all()
    # response_html = '<br>'.join('%s' %id for id in boards)
    # return HttpResponse(response_html)
    return render(request, 'index.html', {'boards': boards})



