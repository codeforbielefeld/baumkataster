import json

from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.views import View

from baumkataster.models import Tree


class TreeView(View):

    http_method_names = ['index', 'get', 'post', 'put', 'delete']

    def index(self):
        trees = Tree.objects.all()
        return JsonResponse([model_to_dict(t) for t in trees], safe=False)

    def get(self, request, pk):
        tree = Tree.objects.get(pk=pk)
        return JsonResponse(model_to_dict(tree))

    def post(self, request):
        print("POST", request)
        data = json.loads(request.body)
        tree = Tree()
        tree.name = data["name"]
        tree.height = data["height"]
        tree.diameter = data["diameter"]
        tree.kind = data["kind"]
        tree.long = data["long"]
        tree.lat = data["lat"]
        tree.type_of_care = data["type_of_care"]
        tree.save()

        # TODO: fix serialization here
        tree.user_list.set(data["user_list"])
        tree.save()

        response = JsonResponse(model_to_dict(tree))
        response.headers["Content-Type"] = "application/json"
        return response

    def put(self, request, pk):
        tree = Tree.objects.get(pk=pk)

        data = json.loads(request.body)
        tree.update(data)

        tree.save(update_fields=["name", "height", "diameter", "kind", "long", "lat", "type_of_care"])

        response = JsonResponse(model_to_dict(tree))
        response.headers["Content-Type"] = "application/json"
        return response

    def delete(self, request, pk):
        tree = Tree.objects.get(pk=pk)
        tree.delete()

        response = HttpResponse("")
        response.status_code = 204
        return response
