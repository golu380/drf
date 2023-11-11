from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Person
from home.serializers import PeopleSerializer

@api_view(['GET','POST','PUT'])
def index(request):
    courses = {
        'course_name':'Python',
        'learn': {'flask','Dango','Tornado','FastApi'},
        'course_provider':'Scaler'
    }
    if request.method == 'GET':
        print(request.GET.get('search'))
        print("you hit a get method")
        return Response(courses)
    elif request.method == 'POST':
        data = request.data
        print(data)
        print("you hit the Post method")
        return Response(courses)
    elif request.method == 'PUT':
        print("you hit the Put method")
        return Response(courses)
    
    
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def person(request):
    if request.method == 'GET':
        # objs = Person.objects.all()
        objs = Person.objects.filter(color__isnull = False)
        serializer = PeopleSerializer(objs,many = True)
        print(serializer.data)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PUT':
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PATCH':
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PeopleSerializer(obj,data = data , partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        data = request.data
        obj = Person.objects.get(id = data['id'])
        obj.delete()
        return Response({'message':'person deleted'})
        
        
        


# Create your views here.
