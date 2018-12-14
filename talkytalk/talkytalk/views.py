from django.shortcuts import render
from django_eventstream import send_event
from django.http import HttpResponse, JsonResponse
from threading import Thread
from time import sleep



def index_render(request):
    return render(request, 'index.html')


def threaded_function(arg):
    for i in range(arg):
        send_event('test', 'message', {'text': 'hello world'})
        sleep(5)


thread = Thread(target=threaded_function, args=(10,))
thread.start()
