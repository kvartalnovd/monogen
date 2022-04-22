from typing import Union

from django.conf import settings
from google.auth.transport import requests
from google.oauth2 import id_token
from rest_framework.exceptions import AuthenticationFailed

from . import BaseAuthService
from .. import serializer, models


class GoogleAuthService:

	TOKEN_DATA_FIELD = 'token'
	EMAIL_DATA_FIELD = 'data'
	
	def __init__(self) -> None:
		self.__baseAuthService = BaseAuthService()

	def check_auth(self, google_user: serializer.GoogleAuth) -> Union[dict, AuthenticationFailed]:
		try:
			id_token.verify_oauth2_token(google_user[self.TOKEN_DATA_FIELD], requests.Request(), settings.GOOGLE_CLIENT_ID)
		except ValueError:
			return AuthenticationFailed(code=403, detail='Google token invalid')

		user, _ = models.AuthUser.objects.get_or_create(email=google_user[self.EMAIL_DATA_FIELD])
		return self.__baseAuthService.createToken(user.id)
