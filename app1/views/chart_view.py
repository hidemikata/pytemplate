from django.shortcuts import render
from django.views.generic import TemplateView
import requests

class ChartView(TemplateView):
    template_name='app1/chart.html'
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        url = 'http://127.0.0.1:8001/get_candle_data'
        head = {'abc': 'def'}
        response = requests.get(url, head)
       
        import json
        data = json.loads(response.text) 
        high = data['high']
        low = data['low']
        prices = data['data']
        candle = '['
        cnt = 0
        for t, p in prices.items():
            cnt+=1
            candle += '['+'\''+t+'\',' + str(p[0]) + ', '+  str(p[1]) + ', '+ str(p[2]) + ', '+ str(p[3]) + '],'
            if cnt==50:
              break 

        candle += ']'
        print(candle)
        ctx['text'] = candle


        return ctx
        


# Create your views here.
