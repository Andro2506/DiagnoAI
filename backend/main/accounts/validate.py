from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken

def validate_access_token(token, user):
    try:
        access_token = AccessToken(token)
        # print("Access Token:")
        # print(access_token)
        # print("user.id:")
        # print(user.id)
        # Ensure the token user matches the provided user
        if access_token['user_id'] != user.id:
            raise InvalidToken("Token does not match the provided user.")
    except TokenError:
        raise InvalidToken("Token is invalid or expired.")