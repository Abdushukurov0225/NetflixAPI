from rest_framework.authtoken.views import obtain_auth_token
from .views import ActorViewSet, MovieViewSet, CommentViewSet, CommentAPIView
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register('movies', MovieViewSet, 'movie')
router.register('actors', ActorViewSet, 'actor')
router.register('comments', CommentViewSet, 'comment')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', obtain_auth_token),
    path('commentsapi/', CommentAPIView.as_view(), name='comments'),
]
