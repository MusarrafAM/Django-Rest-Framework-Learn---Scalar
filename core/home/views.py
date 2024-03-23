from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def index(request):
    course = {
        "course_name": "Python",
        "learn": ["Flask", "Django", "Tornado", "FastApi"],
        "course_provider": "Scaler"
    }

    return Response(course)
