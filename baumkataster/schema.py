import graphene
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType

from baumkataster.models import Tree


class TreeType(DjangoObjectType):
    class Meta:
        model = Tree
        fields = ("oid", "name", "height", "diameter", "long", "lat", "type_of_care", "care_kind", "user_list")


class Query(graphene.ObjectType):
    all_trees_in_radius = graphene.List(
        TreeType,
        lat=graphene.Float(required=True),
        long=graphene.Float(required=True),
        radius=graphene.Float(required=False)
    )

    def resolve_all_trees_in_radius(root, info, lat, long, radius=1):
        return Tree.objects.filter(lat__range=(lat - radius, lat + radius), long__range=(long - radius, long + radius)).all()



schema = graphene.Schema(query=Query)