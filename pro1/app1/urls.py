from django.urls import path
from .views import *


urlpatterns = [
    path('', StudentListApi.as_view())

]
