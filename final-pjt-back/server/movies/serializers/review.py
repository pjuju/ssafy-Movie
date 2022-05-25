from rest_framework import serializers
# from movies.serializers.comment import CommentListSerializer
from accounts.serializers import UserSerializer
from django.contrib.auth import get_user_model
from ..models import Review, Comment, Movie, Genre



class ReviewSerializer(serializers.ModelSerializer):
    class CommentListSerializer(serializers.ModelSerializer):
        class UserSerializer(serializers.ModelSerializer):
            class Meta:
                model = get_user_model()
                fields = ('pk', 'username', 'age',)    
        
        user = UserSerializer(read_only=True)
    
        class Meta:
            model = Comment
            fields = '__all__'    

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
        review_count = serializers.IntegerField(source='reviews.count', read_only=True)    
        watched_count = serializers.IntegerField(source='watched_users.count', read_only=True)
        genres = GenreSerializer(many=True, read_only=True)

        
        class Meta:
            model= Movie
            fields = '__all__'


    movie = MovieSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    like_users = UserSerializer(many=True, read_only=True)
    comments = CommentListSerializer(many=True, read_only=True)
    comments_count = serializers.IntegerField(source='comments.count', read_only=True)


    class Meta:
        model = Review
        fields = '__all__'
       


class ReviewListSerializer(serializers.ModelSerializer):

    class CommentListSerializer(serializers.ModelSerializer):
        class UserSerializer(serializers.ModelSerializer):
            class Meta:
                model = get_user_model()
                fields = ('pk', 'username', 'age',)    
        
        user = UserSerializer(read_only=True)
    
        class Meta:
            model = Comment
            fields = '__all__'    

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
        review_count = serializers.IntegerField(source='reviews.count', read_only=True)    
        watched_count = serializers.IntegerField(source='watched_users.count', read_only=True)
        genres = GenreSerializer(many=True, read_only=True)

        
        class Meta:
            model= Movie
            fields = '__all__'


    movie = MovieSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    like_users = UserSerializer(many=True, read_only=True)
    comments = CommentListSerializer(many=True, read_only=True)
    comments_count = serializers.IntegerField(source='comments.count', read_only=True)


    class Meta:
        model = Review
        fields = '__all__'
        