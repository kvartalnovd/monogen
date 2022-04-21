import jwt

from datetime import timedelta, datetime

from django.conf import settings


class BaseAuthService:

	USER_ID_FIELD = 'user_id'
	TOKEN_TYPE_FIELD = 'token_type'
	ACCESS_TOKEN_FIELD = 'access_token'

	def createToken(self, userId: int) -> dict:
		accessTokenExpires = timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
		return {
			self.USER_ID_FIELD: userId,
			self.ACCESS_TOKEN_FIELD: self.__createAccessToken(
				data={'user_id': userId}, expiresDelta=accessTokenExpires
			),
			self.TOKEN_TYPE_FIELD: 'Token'
		}

	def __createAccessToken(self, data: dict, expiresDelta: timedelta = timedelta(minutes=15)) -> bytes:
		dataToEncode = data.copy()
		expire = datetime.utcnow() + expiresDelta
		dataToEncode.update({'exp': expire, 'sub': 'access'})
		return jwt.encode(dataToEncode, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)