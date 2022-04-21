from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

from components.common.oauth.services import GoogleService

from .. import serializer


class GoogleLogin(View):
	""" Authorization page via google """

	def get(self, request, *args, **kwargs):
		return render(request, template_name='page/oauth/google_login.html', context={'title': 'Авторизация через Google'})


class GoogleOauth(APIView):
	""" Confirmation of authorization via Google """

	__googleService = GoogleService()

	def post(self, request, *args, **kwargs):
		googleData = serializer.GoogleAuth(data=request.data)
		if googleData.is_valid():
			token = self.__googleService.checkAuth(googleData.data)
			return Response(token)

		return AuthenticationFailed(code=403, detail='Google data invalid')