from django.urls import path
from mainapp.views import *

urlpatterns = [
    path('', Home.as_view(), name='home')

]