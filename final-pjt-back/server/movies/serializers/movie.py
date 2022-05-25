from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Movie, Genre
from movies.serializers.review import ReviewListSerializer



class MovieListSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('pk', 'username', 'age',)    


    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = '__all__'
    
    like_users = UserSerializer(many=True, read_only=True)
    watched_users = UserSerializer(many=True, read_only=True)
    reviews = ReviewListSerializer(many=True, read_only=True)    
    review_count = serializers.IntegerField(source='reviews.count', read_only=True)    
    watched_count = serializers.IntegerField(source='watched_users.count', read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
        # 어차피 get만 하니까 read_only_fields 필요 없나?


class MovieSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):

        class Meta:
            model = get_user_model()
            fields = ('pk', 'username', 'age',)    
    
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = '__all__'
            
    like_users = UserSerializer(many=True, read_only=True)
    watched_users = UserSerializer(many=True, read_only=True)
    reviews = ReviewListSerializer(many=True, read_only=True)    
    review_count = serializers.IntegerField(source='reviews.count', read_only=True)   
    liked_count = serializers.IntegerField(source='liked_users.count', read_only=True)
    watched_count = serializers.IntegerField(source='watched_users.count', read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'