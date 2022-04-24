from rest_framework import viewsets, parsers, permissions

from components.common.oauth import serializer, models
from components.common.permissions import IsAuthor


class UserView(viewsets.ModelViewSet):
    """ Viewing and editing user data """

    parser_classes = (parsers.MultiPartParser,)
    serializer_class = serializer.UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user

    def get_object(self):
        return self.get_queryset()


class AuthorView(viewsets.ReadOnlyModelViewSet):
    """ List of authors """

    queryset = models.AuthUser.objects.all()
    serializer_class = serializer.AuthorSerializer


class SocialLinkView(viewsets.ModelViewSet):
    """ CRUD of links and social networks of users """
    serializer_class = serializer.SocialLinkSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        return self.request.user.social_links.all().prefetch_related('social_links')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
