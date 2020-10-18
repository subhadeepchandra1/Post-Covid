
from Profiles.serializers import UserDetailSerializer


def my_jwt_response_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserDetailSerializer(user, context={'request': request}).data
    }