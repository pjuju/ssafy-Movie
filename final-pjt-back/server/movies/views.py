# articles/views.py

from django.shortcuts import get_object_or_404, get_list_or_404
from django.db.models import Count
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie, Review, Comment
from accounts.serializers import UserListSerializer, UserSerializer
from .serializers.movie import MovieListSerializer, MovieSerializer
from .serializers.review import ReviewListSerializer, ReviewSerializer
from .serializers.comment import CommentListSerializer, CommentSerializer
from collections import Counter
import urllib.request
from pprint import pprint
import json
import random

from django.contrib.auth import get_user_model
User = get_user_model()

API_KEY = "e97617d64b251b650b844ce38f163eaa"


@api_view(['GET'])
def movie_list(request):    
    
    movies = Movie.objects.annotate(           
        like_users_count=Count('like_users', distinct=True),
        # watch=Count('like_users', distinct=True)
    )
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)   
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def now_playing(request):    
    request = (f"https://api.themoviedb.org/3/movie/now_playing?api_key={API_KEY}&language=ko")
    response = urllib.request.urlopen(request)
    json_str = response.read().decode('utf-8')
    json_object = json.loads(json_str)         
    return Response(json_object)


@api_view(['GET'])
def upcoming(request):    
    request = (f"https://api.themoviedb.org/3/movie/upcoming?api_key={API_KEY}&language=ko")
    response = urllib.request.urlopen(request)
    json_str = response.read().decode('utf-8')
    json_object = json.loads(json_str)         
    return Response(json_object)

@api_view(['GET'])
def popular(request):    
    request = (f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=ko")
    response = urllib.request.urlopen(request)
    json_str = response.read().decode('utf-8')
    json_object = json.loads(json_str)         
    return Response(json_object)

@api_view(['GET'])
def top_rated(request):    
    request = (f"https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko")
    response = urllib.request.urlopen(request)
    json_str = response.read().decode('utf-8')
    json_object = json.loads(json_str)         
    return Response(json_object)



@api_view(['POST'])
def like_movie(request, movie_pk):    
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user          ## @@@@@@@@@@@@@@@@@@@@@@@@@ 이거 되나?
    if user.like_movies.filter(pk=movie.pk).exists():
        user.like_movies.remove(movie)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    else:
        user.like_movies.add(movie)
        serializer = UserSerializer(user)
        return Response(serializer.data)


@api_view(['POST'])
def watch_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if user.watched_movies.filter(pk=movie.pk).exists():
        user.watched_movies.remove(movie)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    else:
        user.watched_movies.add(movie)
        serializer = UserSerializer(user)
        return Response(serializer.data)



#################### Review
@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.order_by('-pk')
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def review_list_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method =='GET':
        reviews = Review.objects.filter(movie=movie).order_by('-pk')      
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)
    
    elif request.method =='POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def review_detail_delete_update(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)    
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data) 

    elif request.method == 'DELETE':
        review.delete()
        data = {
            'delete': f'리뷰 {review_pk}번이 삭제되었습니다.',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, request.data)        
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data)

@api_view(['POST'])
def review_like(request, movie_pk, review_pk):
    me = request.user
    review = get_object_or_404(Review, pk=review_pk)


    if me.like_reviews.filter(pk=review_pk).exists():
        me.like_reviews.remove(review)
        serializer = UserSerializer(me)
        return Response(serializer.data)
    else:
        me.like_reviews.add(review)
        serializer = UserSerializer(me)
        return Response(serializer.data)
    

################## Comments
@api_view(['GET', 'POST'])
def comment_list_create(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)  
    movie_pk = movie_pk  
    if request.method == 'GET':                
        comments = get_list_or_404(Comment, review_id=review_pk)        
        serializer = CommentListSerializer(comments, many=True)
        # serializer = ReviewSerializer(review)
        return Response(serializer.data)

    if request.method == 'POST':       
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail_upadate_delete(request, movie_pk, review_pk, comment_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review, user=request.user)
            return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        data = {
            'delete': f'리뷰 {comment_pk}번이 삭제되었습니다.',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    
@api_view(['POST'])
def comment_like(request, movie_pk, review_pk, comment_pk):
    me = request.user
    comment = get_object_or_404(Comment, pk=comment_pk)


    if me.like_comments.filter(pk=comment_pk).exists():
        me.like_comments.remove(comment)
        serializer = UserSerializer(me)
        return Response(serializer.data)
    else:
        me.like_comments.add(comment)
        serializer = UserSerializer(me)
        return Response(serializer.data)
    

# recommend
@api_view(['GET'])
def like_list(request):       
    username = request.user.username
    user = get_object_or_404(User, username=username)
    like_movies = user.like_movies        
    serializer = MovieListSerializer(like_movies, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def user_age(request):
    username = request.user.username
    user = get_object_or_404(User, username=username)

    # 같은 연령대로 -2살, +2살로 설정 (+7, -7로 변경 가능)
    min_age, max_age = user.age - 2, user.age + 2

    # 같은 연령대 유저들 가져옴
    user_list = User.objects.filter(age__gte=min_age, age__lte=max_age)
    movie_list = []

    # 같은 연령대 유저들이 시청했거나 좋아요 누른 영화들을 movie_list에 담음
    for user in user_list:       
        like_movies = user.like_movies.all()
        watched_movies = user.watched_movies.all()              
        for like_movie in like_movies:
            movie_list.append(like_movie)
        for watched_movie in watched_movies:
            movie_list.append(watched_movie)
    
    # movie_list에 가장 많이 추가된 영화들 상위 15개 가져옴    
    recommend_movie_list = [i[0] for i in Counter(movie_list).most_common()][:15]
    serializer = MovieListSerializer(recommend_movie_list, many=True)       
    return Response(serializer.data)

@api_view(['GET'])
def user_follow(request):
    username = request.user.username
    user = get_object_or_404(User, username=username)

    # 팔로잉 유저들 가져옴
    user_list = user.followings.all()
    movie_list = []

    # 팔로잉 유저들이 시청했거나 좋아요 누른 영화들을 movie_list에 담음
    for user in user_list:       
        like_movies = user.like_movies.all()
        watched_movies = user.watched_movies.all()              
        for like_movie in like_movies:
            movie_list.append(like_movie)
        for watched_movie in watched_movies:
            movie_list.append(watched_movie)
    
    # movie_list에 가장 많이 추가된 영화들 상위 15개 가져옴
    recommend_movie_list = [i[0] for i in Counter(movie_list).most_common()][:15]
    serializer = MovieListSerializer(recommend_movie_list, many=True)       
    return Response(serializer.data)

@api_view(['GET'])
def user_gender(request):
    username = request.user.username
    user = get_object_or_404(User, username=username) 

    # 성별이 같은 유저들 리스트 가져옴
    user_list = User.objects.filter(gender=user.gender)
    movie_list = []

    # 성별이 같은 유저들이 시청했거나 좋아요 누른 영화들을 movie_list에 담음
    for user in user_list:       
        like_movies = user.like_movies.all()
        watched_movies = user.watched_movies.all()              
        for like_movie in like_movies:
            movie_list.append(like_movie)
        for watched_movie in watched_movies:
            movie_list.append(watched_movie)
    
    # movie_list에 가장 많이 추가된 영화들 상위 15개 가져옴
    recommend_movie_list = [i[0] for i in Counter(movie_list).most_common()][:15]
    
    serializer = MovieListSerializer(recommend_movie_list, many=True)       
    return Response(serializer.data)



@api_view(['GET'])
def like_watch(request):
    username = request.user.username
    user = get_object_or_404(User, username=username)   
    genre_list = []    

    # 내가 좋아요 누른 영화들의 장르들을 장르리스트에 전부 추가       
    for like_movie in user.like_movies.all():
        for genre in like_movie.genres.all():
            genre_list.append(genre)
    
    # 내가 시청한 영화들의 장르들을 장르리스트에 전부 추가
    for watched_movie in user.watched_movies.all()  :
        for genre in watched_movie.genres.all():
            genre_list.append(genre)
    
    # 장르들을 카운트순으로 정렬하여 가장 많이 추가된 장르들 세개를 리스트로 만듬 
    common_genres = [i[0] for i in Counter(genre_list).most_common()][:3]
    
    # 영화데이터에서 장르가 내가 좋아하는 common_geres에 있는 영화들을 populariry로 정렬하여 맨앞 15개 가져옴 
    movie_list = Movie.objects.filter(genres__in=common_genres, vote_count__gte=5000).distinct().order_by('-vote_count')[:15]  
    serializer = MovieListSerializer(movie_list, many=True)       
    return Response(serializer.data)


@api_view(['GET'])
def search_list(request, title):
    print(title)
    movies = Movie.objects.filter(title__contains=title) | Movie.objects.filter(original_title__contains=title)
    movies = movies.distinct().order_by('-popularity')
    serializer = MovieListSerializer(movies, many=True)       
    return Response(serializer.data)