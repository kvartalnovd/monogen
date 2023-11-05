from typing import Union

from django.conf import settings
from google.auth.transport import requests
from google.oauth2 import id_token
from rest_framework.exceptions import AuthenticationFailed 

from components.common.oauth.models import AuthUser
from components.common.oauth.serializer import GoogleAuthSerializer
from components.common.oauth.services.base_oauth import BaseAuthService


class GoogleAuthService:

	TOKEN_DATA_FIELD = 'token'
	EMAIL_DATA_FIELD = 'email'
	
	def __init__(self) -> None:
		self.__baseAuthService = BaseAuthService()

	def check_auth(self, google_user: GoogleAuthSerializer) -> Union[dict, AuthenticationFailed]:
		try:
			id_token.verify_oauth2_token(google_user[self.TOKEN_DATA_FIELD], requests.Request(), settings.GOOGLE_CLIENT_ID)
		except ValueError:
			return AuthenticationFailed(code=403, detail='Google token invalid')

		user, _ = AuthUser.objects.get_or_create(email=google_user[self.EMAIL_DATA_FIELD])
		return self.__baseAuthService.create_token(user.id)
