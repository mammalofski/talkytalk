from django.views.generic import TemplateView


from django_eventstream import send_event
send_event('testChannel', 'message', {'text': 'hello world'})

class Index(TemplateView):
    template_name = 'index.html'

