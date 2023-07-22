from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from film.models import Actor, Movie, Comment
from film.serializers import ActorsSerializer, MoviesSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorsSerializer

class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['genre']
    ordering_fiels = ['imdb', '-imdb']
    search_fields = ['name']


    @action(detail=True, methods=['POST'])
    def add_actor(self, request, *args, **kwargs):
        movie = self.get_object()
        actor_id = request.data

        if actor_id['actor'] not in movie.actor.all():
            movie.actor.add(actor_id['actor'])
            serializer = ActorsSerializer(movie.actor.all(), many=True)

            return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def remove_actor(self, request, *args, **kwargs):
        movie = self.get_object()
        actor_id = request.data.get('actor')
        movie.actor.remove(actor_id)

        serializer = ActorsSerializer(movie.actor.all(), many=True)
        return Response(serializer.data)


class MovieActorAPIView(APIView):
    def get(self, request):
        movie = Movie.objects.all()
        serializer = MoviesSerializer(movie, many=True)

        return Response(serializer.data)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    authentication_classes =(TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


    def get_queryset(self):
        return Comment.objects.filter(user_id=self.request.user)

    def perform_create(self, serializer):
        serializer.validated_data['user_id'] = self.request.user
        serializer.save()

class CommentAPIView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def delete(self, request):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        comment = Comment.objects.get(id = request.data['id'])
        comment.delete()

        return Response(serializer.data)

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)


        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)