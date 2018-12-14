from django.shortcuts import render
from django_eventstream import send_event
from django.http import HttpResponse, JsonResponse


def start_stream(request):
    return send_event('testChannel', 'message', {'text': 'hello world'})


def index_render(request):
    return render(request, 'index.html')




