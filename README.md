# 1. Model

- ## 1. User (Accounts)

  1) username
  2) password
  3) age
  4) sex

  -----

  1. followings

  2. followed

  3. like_movies

  4. reviews

  5. like_reviews

  6. comments

  7. like_comments

     

     

     

- ## 2. Movies (Movies)

  1. title

  2. overview

  3. like_users (주 관심 연령대)

  3. watched_users (주 시청 연령대)

  3. reviews

  4. release_date

  5. poster_path

  6. popularity

  7. vote_count

  8. vote_average

     

- ## 3. Review(=>Movies)

  1. user
  2. like_users
  3. title
  4. content
  5. movie
  6. created_at
  7. updated_at

- ## 3. Comments (=>Review)

  1. user
  2. like_user
  3. Review

# 2. 기능

## 	1. Accounts

- 1. signup
  2. login
  3. logout
  4. profile
     - follow
     - like_movies
     - recommened_movies (가장 마지막에 하자)
       - 1. 팔로우 한 유저들이 시청한 영화
         2. 동 나이대 유저들이 시청한 영화
         3. 내가 많이 본 장르의 영화
         4. 좋아하는 배우가 나오는 영화?
     - reviews
     - comments
  5. reset

URL: accounts/:username/()

## 2. Movies

- 1. MovieList
     1. Random
     2. 평점 순
     3. 관객 순
     4. 최근 개봉한 영화
     5. 날씨 추천
     6. 계절 추천
     7. recommened_movies (가장 마지막에 구현)
        - 1. 팔로우 한 유저들이 시청한 영화
          2. 동 나이대 유저들이 시청한 영화
          3. 내가 많이 본 장르의 영화
          4. 좋아하는 배우가 나오는 영화?
- 2. MovieDetail
     1. Movie
        1. Review (order_by -pk, like_count)
        2. Movie 필드
        3. 예고영상

# 3. Review

1. ReviewList (Review탭에 들어가는 것. order_by [-pk, like_count]

2. ReviewDetail (ReviewList, MovieDetail에 들어가는 것)

   1. Create

   2. Delete

   3. Update

   4. Like

   

- Comments
  - create
  - delete
  - like



URL : /movies/:movie_pk/review/:review_pk/comment/:comment_pk



## 3. 페이지 구성

- navbar
  - signup
  - login/logout
  - myprofile
  - movieSearchForm

https://www.youtube.com/results?search_query=%EC%95%84%EC%A0%80%EC%94%A8

1. Profile => URL/accounts/:username
   1. myReviewList
   2. myCommentList
   3. userSearchForm
2. MovieList => URL/movies/
   1. ReviewList(넣어도 되고 안넣어도 됨)
3. MovieDetail => URL/movie/:movie_pk
   1. movieReviewList
   2. movieReviewForm
4. ReviewDetail => URL/movie/:movie_pk/review/:review_pk
   1. ReviewCommentList
   2. ReviewCommentForm



1. View
   - ProfileView
   - 

2. Component





