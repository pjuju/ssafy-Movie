from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from movies.models import Movie, Review, Comment


class FakeUserSerializer(serializers.ModelSerializer):
    class MovieListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = '__all__'

    class ReviewListSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Review
            fields = '__all__'

    
    class CommentListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = '__all__'

    like_movies = MovieListSerializer(many=True, read_only=True)
    watched_movies = MovieListSerializer(many=True, read_only=True)   
    reviews = ReviewListSerializer(many=True, read_only=True)
    like_reviews = ReviewListSerializer(many=True, read_only=True)
    comments = CommentListSerializer(many=True, read_only=True)
    like_comments = CommentListSerializer(many=True, read_only=True)
    
    class Meta:
        model = get_user_model()        
        fields = '__all__'


class UserSerializer(FakeUserSerializer):
    followings = FakeUserSerializer(many=True, read_only=True)
    followers = FakeUserSerializer(many=True, read_only=True)

    class Mete:
        model = get_user_model()
        fields = '__all__'


class UserListSerializer(FakeUserSerializer):

    class MovieListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = '__all__'

    like_movies = MovieListSerializer(many=True, read_only=True)
    watched_movies = MovieListSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = '__all__'

class CustomRegisterSerializer(RegisterSerializer):
    # 기본 설정 필드: username, password, email
    # 추가 설정 필드: profile_image
    age = serializers.IntegerField()
    gender = serializers.CharField(max_length=6)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['age'] = self.validated_data.get('age', '')
        data['gender'] = self.validated_data.get('gender', '')

        return data