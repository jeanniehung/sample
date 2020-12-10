from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from .models import Board

# Create your views here.


def index(request):
    boards = Board.objects.all()
    # response_html = '<br>'.join('%s' %id for id in boards)
    # return HttpResponse(response_html)
    return render(request, 'index.html', {'boards': boards})


def board_topics(request, pk):
    # try:
    #     board = Board.objects.get(pk=pk)
    # except Board.DoesNotExist:
    #     raise Http404
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})




