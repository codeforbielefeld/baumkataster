import datetime

import graphene
import jwt
from django.contrib.auth.models import User
from graphql import GraphQLError

from baumkataster.graphql.types.UserType import UserType


class CreateUserMutation(graphene.Mutation):
    user = graphene.Field(UserType)
    token = graphene.String()

    class Arguments:
        email = graphene.String(required=True)
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)

    def mutate(self, root, info, email, username, password, first_name, last_name):
        if not User.objects.exists(username=username):
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            encoded_jwt = jwt.encode({
                "sub": user.id,
                "name": f"{user.first_name} {user.last_name}",
                "iat": datetime.datetime.now(tz=datetime.timezone.utc),
                "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days=30),
            }, "secret", algorithm="HS256")  # TODO: Find a good spot for a secret key

            print(encoded_jwt)
            return CreateUserMutation(user=user, token=encoded_jwt)
        else:
            print("User already exists")
            raise GraphQLError(f"User already exists")
