const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'
const REVIEWS = 'reviews/'
const COMMENTS = 'comments/'
const RECOMMEND = 'recommend/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    follow: username => HOST + ACCOUNTS + 'follow/' + `${username}/`,
    profile: username => HOST + ACCOUNTS + 'profile/' + `${username}/`,
    // 유저 로그인 확인
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
  },
  movies: {
    movies: () => HOST + MOVIES,
    movie: moviePk => HOST + MOVIES + `${moviePk}/`,
    likemovie: moviePk => HOST + MOVIES + `${moviePk}/` + 'like/',
    watchedmovie: moviePk => HOST + MOVIES + `${moviePk}/` + 'watch/',

    // 그냥 영화들
    nowPlaying: () => HOST + MOVIES + 'now_playing/',
    upcoming: () => HOST + MOVIES + 'upcoming/',
    popular: () => HOST + MOVIES + 'popular/',

    // 알고리즘
    likemovies: (username) => HOST + MOVIES + 'like_list/' + `${username}/`,
    likewatchedmovies: (username) => HOST + MOVIES + RECOMMEND + `${username}/` + 'like_watch/',
    gendermovies: (username) => HOST + MOVIES + RECOMMEND + `${username}/` + 'user_gender/',
    agemovies: (username) => HOST + MOVIES + RECOMMEND + `${username}/` + 'user_age/',
    followmovies: (username) => HOST + MOVIES + RECOMMEND + `${username}/` + 'user_follow/',



    reviewList: () => HOST + MOVIES + REVIEWS, //전체 리뷰가져오기
    reviews: moviePk => HOST + MOVIES + `${moviePk}/` + REVIEWS,
    review: (moviePk, reviewPk) => HOST + MOVIES + `${moviePk}/` + REVIEWS + `${reviewPk}/`,
    reviewlike: (moviePk, reviewPk) => HOST + MOVIES + `${moviePk}/` + REVIEWS + `${reviewPk}/` + 'like/',

    comments: (moviePk, reviewPk) => HOST + MOVIES + `${moviePk}/` + REVIEWS + `${reviewPk}/` + COMMENTS,
    comment: (moviePk, reviewPk, commentPk) =>  HOST + MOVIES + `${moviePk}/` + REVIEWS + `${reviewPk}/` + COMMENTS + `${commentPk}/`,
    commentlike: (moviePk, reviewPk, commentPk) => HOST + MOVIES + `${moviePk}/` + REVIEWS + `${reviewPk}/` + COMMENTS + `${commentPk}/` +'like/'
  },
}