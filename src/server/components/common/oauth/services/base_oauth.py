from datetime import timedelta, datetime

import jwt
from django.conf import settings


class BaseAuthService:

	USER_ID_FIELD = 'user_id'
	TOKEN_TYPE_FIELD = 'token_type'
	ACCESS_TOKEN_FIELD = 'access_token'

	def create_token(self, user_id: int) -> dict:
		access_token_expires = timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
		return {
			self.USER_ID_FIELD: user_id,
			self.ACCESS_TOKEN_FIELD: self.__create_access_token(
				data={'user_id': user_id}, expires_delta=access_token_expires
			),
			self.TOKEN_TYPE_FIELD: 'Token'
		}

	@classmethod
	def __create_access_token(cls, data: dict, expires_delta: timedelta = timedelta(minutes=15)) -> bytes:
		data_to_encode = data.copy()
		expire = datetime.utcnow() + expires_delta
		data_to_encode.update({'exp': expire, 'sub': 'access'})
		return jwt.encode(data_to_encode, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)