from rest_framework import serializers

from components.common.oauth import models


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.AuthUser
		fields = ('avatar', 'country', 'city', 'bio', 'display_name')


class GoogleAuthSerializer(serializers.Serializer):
	""" Serialization of data from Google """

	email = serializers.EmailField()
	token = serializers.CharField()
