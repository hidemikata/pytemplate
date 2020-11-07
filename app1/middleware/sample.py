class SampleMiddleware() :
    def __init__(self, get_response) :
        self.get_response = get_response
  
    def __call__(self, request) :
        print('__call__ before view')
        response = self.get_response(request)#>>view
        print('__call__ after view')
        return response
  
  #beforefilter
    def process_view(self, request, func, args, kwargs):
        print('process_view')
        print(func.__name__.startswith('A'))#関数名がAから始まる
        token = request.GET.get('token')
        if not token :
            print('token invalid')

    #beforerender
    def process_template_response(self, request, response):
        print('process_template_response')
        response.context_data['title'] = 'kyoutuu title'
        return response
  
