from rest_framework import serializers


class GoogleAuth(serializers.Serializer):
	""" Serialization of data from Google """

	email = serializers.EmailField()
	token = serializers.CharField()