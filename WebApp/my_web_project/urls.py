from django.urls import path
from . import views

urlpatterns = [
    # path('',views.index,name="index"),
    path('', views.indexPageView.as_view(template_name="pages/index.html")),
    path('basemain/', views.homePageView.as_view(template_name="pages/home.html")),
    path('students/', views.StudentListView.as_view(template_name="pages/students.html")),
    path('hello/', views.hello_students),
]
