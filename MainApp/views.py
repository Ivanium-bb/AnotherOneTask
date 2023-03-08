from rest_framework import status, mixins
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken

from .models import Notes
from .serializers import UserSerializer, NotesSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # refresh = RefreshToken.for_user(dict(serializer.data))
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def authentication_test(request):
    print(request.user)
    return Response(
        {
            'message': "User successfully authenticated"
        },
        status=status.HTTP_200_OK,
    )


class LogoutView(APIView):
    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)


class NotesViewSet(ModelViewSet):
    serializer_class = NotesSerializer
    lookup_field = 'id'

    def get_queryset(self):
        author = int(self.request.auth.payload['user_id'])
        queryset = Notes.objects.filter(author=author)
        return queryset

    def create(self, request, *args, **kwargs):
        author = int(request.auth.payload['user_id'])
        request.data._mutable = True
        request.data['author'] = author
        request.data._mutable = False
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        author = int(request.auth.payload['user_id'])
        request.data._mutable = True
        request.data['author'] = author
        request.data._mutable = False
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
