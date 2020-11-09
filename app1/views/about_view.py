from django.shortcuts import render
from django.views.generic import TemplateView
from app1.models.topic import Topic


class AboutView(TemplateView):
    template_name='app1/about.html'
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['message'] = 'this is get.'
        ctx['all'] = Topic.objects.all()
        #where (hairetu de toreru)
        ctx['id2'] = Topic.objects.filter(id=2)
        getid = Topic.objects.get(id=2)
        getid.value=3
        #update set
        getid.save()
        ctx['getid'] = getid
        #insert into 
        Topic(value=1, question_text='question_text', pub_date='2020-11-10 00:00:00.000000').save()
        return ctx
    def post(self, request, *args, **kwargs):
        ctxt= {
          'message':'post method ok!!',
          'name':request.POST['name']
        }
        return render(request, 'app1/about.html', ctxt)

        


# Create your views here.
