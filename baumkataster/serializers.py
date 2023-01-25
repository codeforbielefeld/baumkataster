from rest_framework import serializers

from baumkataster.models import Tree


class TreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tree
        fields = '__all__'
