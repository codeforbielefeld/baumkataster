from django.http import JsonResponse
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from baumkataster.views.TreeView import TreeView

def hello_world(request):
    return JsonResponse({'message': 'Hallo Bielefeld!'})


urlpatterns = [
    path('hello', hello_world),
    path('trees', csrf_exempt(TreeView.as_view())), #accesses tree-database and understands what we want to do (e.g. add/index/put...)
    path('trees/<int:id>', csrf_exempt(TreeView.as_view())) #enables user to access specific tree by id
]
