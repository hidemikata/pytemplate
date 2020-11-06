from django.shortcuts import render
from django.views.generic import TemplateView
import requests

class RequestView(TemplateView):
    template_name='app1/request.html'
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        url = 'https://example.com/'
        head = {'abc': 'def'}
        response = requests.get(url, head)
        ctx['code'] = response.status_code
        ctx['url'] = response.url
        ctx['head'] = response.headers
        ctx['text'] = response.text

        return ctx
        


# Create your views here.
