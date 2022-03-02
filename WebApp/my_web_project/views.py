from django.http import HttpResponse
from django.views.generic import ListView, TemplateView, FormView
from .models import Students

from rest_framework.response import Response
from rest_framework.decorators import api_view


def index(response):
    return HttpResponse("This message is from views ")


class indexPageView(TemplateView):
    template_name = "pages/index.html"


class homePageView(TemplateView):
    template_name = "pages/home.html"


class StudentListView(ListView):
    template_name = 'pages/students.html'

    def get_queryset(self):
        queryset = Students.objects.all()

        return queryset


@api_view(['GET', 'POST'])
def hello_students(request):
    if request.method == 'POST':
        return Response({"message": "New data!", "data": request.data})
    return Response({"message": "Hello, students!"})
