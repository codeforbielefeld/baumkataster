from django.http import JsonResponse
from django.urls import path
from graphene_django.views import GraphQLView


from baumkataster.views.SingleTreeView import SingleTreeView
from baumkataster.views.TreesView import TreesView


def hello_world():
    return JsonResponse({'message': 'Hallo Bielefeld!'})


urlpatterns = [
    path('hello', hello_world),
    path('', TreesView.as_view()),
    path('<str:pk>', SingleTreeView.as_view()),
]
