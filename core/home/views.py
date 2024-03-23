from rest_framework.decorators import api_view
from rest_framework.response import Response

from home.models import Person
from .serializers import PeopleSerializer

# For example only i added these 3 methods , here GET only enough


@api_view(["GET", "POST", "PUT"])
def index(request):
    course = {
        "course_name": "Python",
        "learn": ["Flask", "Django", "Tornado", "FastApi"],
        "course_provider": "Scaler"
    }

    if request.method == "GET":
        print("Your Query parame output is below")
        print(request.GET.get("search"))
        print("You hit GET method")
        return Response(course)
    elif request.method == "POST":
        # we use this request.data for put post patch but for get request passing data we use query parames
        # we acces it in the above manner.
        data = request.data
        print("*********")
        print(data)
        print("*********")
        print("You hit POST method")
        return Response(course)
    elif request.method == "PUT":
        print("You hit PUT method")
        return Response(course)


@api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
def person(requset):
    if requset.method == "GET":
        objs = Person.objects.all()
        serializer = PeopleSerializer(objs, many=True)
        return Response(serializer.data)

    elif requset.method == "POST":
        data = requset.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():   # Check the data coming from the user is serializable (if have all the fields)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif requset.method == "PUT":
        data = requset.data
        obj = Person.objects.get(id=data['id'])
        # Passing the object that need to update and the data we need to puy
        serializer = PeopleSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif requset.method == "PATCH":
        data = requset.data
        obj = Person.objects.get(id=data['id'])
        # Enable partial Update for PATCH
        serializer = PeopleSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif requset.method == "DELETE":
        data = requset.data
        obj = Person.objects.get(id=data['id'])
        obj.delete()
        return Response({"Message": "Person Deleted Succesfully"})
