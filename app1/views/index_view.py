from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
import app1.constants as const
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

        #プロジェクトのコンフィグから定数取得
        print(getattr(settings, "TEST_URL", None))
        #app共通にconstantを作って定数取得。
        print(const.TEST_URL2)
        return ctx


# Create your views here.
