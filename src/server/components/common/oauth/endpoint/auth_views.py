from django.shortcuts import render
from django.views.generic import View
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from components.common.oauth import serializer
from components.common.oauth.services.google_auth import GoogleAuthService


class GoogleLogin(View):
	""" Authorization page via google """

	def get(self, request, *args, **kwargs):
		return render(request, template_name='page/oauth/google_login.html', context={'title': 'Авторизация через Google'})


class GoogleOauth(APIView):
	""" Confirmation of authorization via Google """

	__googleAuthService = GoogleAuthService()

	def post(self, request, *args, **kwargs):
		google_data = serializer.GoogleAuthSerializer(data=request.data)
		if google_data.is_valid():
			token = self.__googleAuthService.check_auth(google_data.data)
			return Response(token)

		return AuthenticationFailed(code=403, detail='Google data invalid')