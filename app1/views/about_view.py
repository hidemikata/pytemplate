from django.shortcuts import render
from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name='app1/about.html'
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['message'] = 'this is get.'
        return ctx
    def post(self, request, *args, **kwargs):
        ctxt= {
          'message':'post method ok!!',
          'name':request.POST['name']
        }
        return render(request, 'app1/about.html', ctxt)

        


# Create your views here.
