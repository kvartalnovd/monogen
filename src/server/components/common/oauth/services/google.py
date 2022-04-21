import email
from google.oauth2 import id_token
from google.auth.transport import requests

from django.conf import settings

from rest_framework.exceptions import AuthenticationFailed

from components.common.oauth.models import AuthUser
from . import BaseAuthService
from .. import serializer



class GoogleService:

	TOKEN_DATA_FIELD = 'token'
	EMAIL_DATA_FIELD = 'data'
	
	def __init__(self) -> None:
		self.initServices()
	
	def initServices(self) -> None:
		self.__baseAuthService = BaseAuthService()

	def checkAuth(self, googleUser: serializer.GoogleAuth) -> dict:
		try:
			id_token.verify_oauth2_token(googleUser.get(self.TOKEN_DATA_FIELD), requests.Request(), settings.GOOGLE_CLIENT_ID)
		except ValueError:
			return AuthenticationFailed(code=403, detail='Google token invalid')
		
		user, _ = AuthUser.objects.get_or_create(email=googleUser.get(self.EMAIL_DATA_FIELD))
		return self.__baseAuthService.createToken(user.id)