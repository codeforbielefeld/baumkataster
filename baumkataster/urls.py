from django.urls import path
from baumkataster.views import add_tree, hello_world


urlpatterns = [
    path('hello', hello_world),
    path('add_tree', add_tree)
]
