from django.urls import path
from . import views

urlpatterns = [
    path('', views.tutorial, name='tutorial'),
    path('my_tutorials', views.my_tutorials, name='my_tutorials'),
    path('my_tutorials/tutorial_detail/<int:id>', views.tutorial_detail, name='tutorial_detail'),
]