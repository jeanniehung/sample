from django.shortcuts import render
from django.http import HttpResponse
from .models import Board


# Create your views here.


# def index(request):
#     boards = Board.objects.all()
#     boards_names = []
#     for board in boards:
#         boards_names.append(board.name)
#     response_html = '<br>'.join(boards_names)
#     return HttpResponse(response_html)

def index(request):
    boards = Board.objects.all()
    return render(request, 'index.html', {'boards': boards})


def board_topics(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'topics.html', {'board': board})










