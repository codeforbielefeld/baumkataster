from django.http import JsonResponse
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from baumkataster.views.TreeView import TreeView

def hello_world(request):
    return JsonResponse({'message': 'Hallo Bielefeld!'})


urlpatterns = [
    path('hello', hello_world),
    path('trees', csrf_exempt(TreeView.index), name='index'),
    path('add', csrf_exempt(TreeView.as_view())),
    path('trees/<int:id>', csrf_exempt(TreeView.as_view())),
]
