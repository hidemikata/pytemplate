from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name='app1/index.html'
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['testctx'] = ['a','b','c','d',]
        ctx['id'] = 3
#クエリー。
#        print(self.request.GET)
#header
#        print(self.request.META['HTTP_USER_AGENT'])
        return ctx


# Create your views here.
