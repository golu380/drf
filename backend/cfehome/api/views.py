
from products.models import Product
from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.Serializers import ProductSerializers

#django module
@api_view(["GET"])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        data  = ProductSerializers(instance).data
    return Response(data)

@api_view(["POST"])
def api_homepost(request, *args , **kwargs):
    
    serializer = ProductSerializers(data = request.data)
    if serializer.is_valid():
        data = serializer.save()
        print(data)
        return Response(data)
    return None
    
    


# Create your views here.

# def api_home(request,*args,**kwargs):
#     body = request.body # byte string of json data
#     print(body)
#     print(request.GET)
#     print(request.POST)
#     data = {}
#     try:
#         data = json.loads(body) # takes string of json data ->python dictionary
#     except:
#         pass
#     print(data)
#     print(data.keys())
#     data['headers'] = dict(request.headers)
#     data['params'] = dict(request.GET)
    
#     data['content_type'] = request.content_type
#     print(data)
#     return JsonResponse({"message":"Hi there , this si your django api response !!"})


# @api_view(["GET"])
# def api_home(request,*args, **kwargs):
    
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         # data['id'] = model_data.id
#         # data['title'] = model_data.title
#         # data['content'] = model_data.content
#         # data['price'] = model_data.price
#         data = model_to_dict(model_data,fields=['id','title','price','sale_price'])
#     return Response(data)
#     #     json_data_star  = json.dumps(data)
#     #     print(data)
#     # return HttpResponse(json_data_star,headers={'content-type':'application/json'})
#     # return JsonResponse(data)