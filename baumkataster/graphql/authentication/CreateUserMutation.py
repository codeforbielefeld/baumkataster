import datetime

import graphene
import jwt
from django.contrib.auth.models import User
from graphql import GraphQLError

from baumkataster.graphql.types.UserType import UserType


class CreateUserMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)

    user = graphene.Field(UserType)
    token = graphene.String()

    @classmethod
    def mutate(self, root, info, email, username, password, first_name, last_name):
        try:
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            encoded_jwt = jwt.encode({
                "sub": user.id,
                "name": f"{user.first_name} {user.last_name}",
                "iat": datetime.datetime.now(tz=datetime.timezone.utc),
                "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days=30),
            }, "secret", algorithm="HS256") # TODO: Find a good spot for a secret key

        except Exception as e:
            print(e)
            raise GraphQLError("User already exists")
        return CreateUserMutation(user=user, token=encoded_jwt)