from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from film.models import Actor, Movie, Comment
import datetime

class ActorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

    def validate_birthdate(self, value):
        if value < datetime.date(1950, 1, 1):
            raise ValidationError(detail="Birthdate less '1950-01-01'")
        return value

class MoviesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
