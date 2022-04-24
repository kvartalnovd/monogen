from rest_framework import serializers

from components.common.oauth import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AuthUser
        fields = ('avatar', 'country', 'city', 'bio', 'display_name')


class SocialLinkSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.UserSocialLink
        fields = ('id', 'link',)


class AuthorSerializer(serializers.ModelSerializer):
    social_links = SocialLinkSerializer(many=True)

    class Meta:
        model = models.AuthUser
        fields = ('id', 'avatar', 'country', 'city', 'bio', 'display_name', 'social_links')


class GoogleAuthSerializer(serializers.Serializer):
    """ Serialization of data from Google """

    email = serializers.EmailField()
    token = serializers.CharField()

