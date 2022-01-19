from atexit import register
import graphene
from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations

class AuhMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    
class Query(UserQuery, MeQuery, graphene.ObjectType):
    pass

class Mutation(AuhMutation, graphene.ObjectType):
    pass
schema = graphene.Schema(query=Query, mutation=Mutation)