from django.urls import path
from baumkataster.views import hello_world


urlpatterns = [
    path('hello', hello_world),
]
