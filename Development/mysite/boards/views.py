from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from .models import Board, Post, Topic


# Create your views here.
def home(request):
    boards = Board.objects.all()
    # response_html = '<br>'.join('%s' %i for i in boards)
    # return HttpResponse(response_html)
    return render(request, 'home.html', {'boards': boards})


def board_topics(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'topics.html', {'board': board})

