from datetime import datetime

from rest_framework import generics, status
from rest_framework.response import Response

from baumkataster.models import Tree
from baumkataster.serializers import TreeSerializer


class SingleTreeView(generics.GenericAPIView):
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer

    def get_tree(self, pk):
        try:
            return Tree.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        tree = self.get_tree(pk=pk)
        if tree == None:
            return Response({"status": "fail", "message": f"Tree with Id: {pk} not found"},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(tree)
        return Response({"status": "success", "tree": serializer.data})

    def patch(self, request, pk):
        tree = self.get_tree(pk)
        if tree == None:
            return Response({"status": "fail", "message": f"Tree with Id: {pk} not found"},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            tree, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status": "success", "note": serializer.data})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tree = self.get_tree(pk)
        if tree == None:
            return Response({"status": "fail", "message": f"Tree with Id: {pk} not found"},
                            status=status.HTTP_404_NOT_FOUND)

        tree.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
