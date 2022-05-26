from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # movies
    path('', views.movie_list), # 전체 영화리스트 O
    path('serach_list/<title>/', views.search_list), # 영화 검색 리스트  
    path('like_list/', views.like_list), # 좋아요 누른 영화리스트    
    path('now_playing/', views.now_playing), # 전체 현재 상영작
    path('upcoming/', views.upcoming), # 상영예정작
    path('popular/', views.popular), # 인기작    
    path('top_rated/', views.top_rated), # 평점 높은 작
    path('<int:movie_pk>/', views.movie_detail), # 상세 영화 정보 O    
    path('<int:movie_pk>/like/', views.like_movie), # like O
    path('<int:movie_pk>/watch/', views.watch_movie), # watch 체크 O
    
    # reviews
    path('reviews/', views.review_list), #전체 리뷰 리스트 O
    path('<int:movie_pk>/reviews/', views.review_list_create), # 영화별 리뷰리스트, 생성 O
    path('<int:movie_pk>/reviews/<int:review_pk>/', views.review_detail_delete_update), # 상세 리뷰, 삭제, 업뎃 O
    path('<int:movie_pk>/reviews/<int:review_pk>/like/', views.review_like), # 리뷰 좋아요
    
    # comments
    path('<int:movie_pk>/reviews/<int:review_pk>/comments/', views.comment_list_create), # 영화 -> 리뷰 -> 댓글리스트
    path('<int:movie_pk>/reviews/<int:review_pk>/comments/<int:comment_pk>/', views.comment_detail_upadate_delete), # 상세 댓글
    path('<int:movie_pk>/reviews/<int:review_pk>/comments/<int:comment_pk>/like/', views.comment_like), # 댓글 좋아요

    # recommend
    path('recommend/user_age/', views.user_age), # 내 나이대 유저들이 찜하거나 시청한 영화
    path('recommend/user_gender/', views.user_gender), # 내 성별 유저들이 찜하거나 시청한 영화
    path('recommend/user_follow/', views.user_follow), # 내가 팔로우한 유저들이 찜하거나 시청한 영화  
    path('recommend/like_watch/', views.like_watch), # 내가 찜한/시청한 영화들과 유사한 유사한 영화
    
    



   
]
