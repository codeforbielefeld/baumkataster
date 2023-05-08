from graphene_django import DjangoObjectType

from django.contrib.auth.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
