from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework_jwt.settings import api_settings


# define user module
User = get_user_model()


class ApiMan:
    def __init__(self, user=None):
        self.user = user

        # create user if None is provided
        if not self.user:
            self.user = User.objects.create_user(
                username='admin_user_api',
                email='admin_user_api@mail.com',
                password='pass')

    def getClientJWT(self):
        """
        return an APIClient (from rest_framework) with JWT credentials
        """
        # api client
        client = APIClient()

        # jwt handle
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        # create token
        payload = jwt_payload_handler(self.user)
        token = jwt_encode_handler(payload)

        # set credentials
        client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

        return client
