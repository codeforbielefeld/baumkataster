from django.http import JsonResponse
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from baumkataster.models import Tree
from django.forms.models import model_to_dict

# Create your views here.

def hello_world(request):
	return JsonResponse({'message':'Hallo Bielefeld!'})

@csrf_exempt
def add_tree(request):
	if request.method == "POST":

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
		tree.user_list.set(data["user_list"])
		tree.save()

		return JsonResponse(model_to_dict( tree ))