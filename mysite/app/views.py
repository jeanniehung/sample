from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    # string = u'default ...'
    # TutorialList = ['pycharm', 'xmind', 'google', 'ie', 'file']
    # TutorialDict = {'jane': 21, 'yoyo': 34, 'sim': 17}
    # List = map(lambda x: x ** 2, range(100))
    EmptyList = []
    return render(request, "home.html", {'EmptyList': EmptyList})
