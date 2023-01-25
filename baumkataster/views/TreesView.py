import math

from rest_framework import generics, status
from rest_framework.response import Response

from baumkataster.models import Tree
from baumkataster.serializers import TreeSerializer


class TreesView(generics.GenericAPIView):
    serializer_class = TreeSerializer
    queryset = Tree.objects.all()

    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        trees = Tree.objects.all()
        total_trees = trees.count()
        if search_param:
            trees = trees.filter(title__icontains=search_param)
        serializer = self.serializer_class(trees[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_trees,
            "page": page_num,
            "last_page": math.ceil(total_trees / limit_num),
            "trees": serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "tree": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
