from django.shortcuts import render

# Create your views here.
from logs.models import LogModel


def index(request):
    ctx = {}
    ctx['logs'] = LogModel.objects.all()
    return render(request, 'main.html', ctx)
