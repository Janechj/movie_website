from django.urls import path

from moviesystem.views import DirectorList, MovieList, ReviewList, ActorList, MovieDetail, DirectorDetail, ActorDetail, \
    Myprofile, Home, ReviewUpdate, ReviewDelete, MyprofileUpdate, Login, yearsmovie, Recommendation

from . import views

urlpatterns = [
    path('recommendations/', Recommendation.as_view(), name='recommendations'),

    path('director/',
         DirectorList.as_view(),
         name='moviesystem_director_list_urlpattern'),

    path('director/<int:pk>/',
         DirectorDetail.as_view(),
         name='moviesystem_director_detail_urlpattern'),

    path('movie/',
         MovieList.as_view(),
         name='moviesystem_movie_list_urlpattern'),

    path('movie/<int:pk>/',
         MovieDetail.as_view(),
         name='moviesystem_movie_detail_urlpattern'),

    path('review/',
         ReviewList.as_view(),
         name='moviesystem_review_list_urlpattern'),

    path('movie/<int:pk>/review/',
         views.add_review_to_movie,
         name='add_review_to_movie'),

    path('yearsmovie/',
         yearsmovie.as_view(),
         name='moviesystem_yearsmovie_urlpattern'),

    path('review/<int:pk>/update/',
         ReviewUpdate.as_view(),
         name='moviesystem_review_update_urlpattern'),

    path('review/<int:pk>/delete/',
         ReviewDelete.as_view(),
         name='moviesystem_review_delete_urlpattern'),

    path('actor/',
         ActorList.as_view(),
         name='moviesystem_actor_list_urlpattern'),

    path('actor/<int:pk>/',
         ActorDetail.as_view(),
         name='moviesystem_actor_detail_urlpattern'),

    path('myprofile/<int:pk>/',
         Myprofile.as_view(),
         name='moviesystem_myprofile_urlpattern'),

    path('myprofile/<int:pk>/update',
         MyprofileUpdate.as_view(),
         name='moviesystem_myprofile_update_urlpattern'),

    path('home/',
         Home.as_view(),
         name='moviesystem_home_urlpattern'),

    path('login/', Login.as_view(), name='moviesystem_login_urlpattern'),

    path('userSearch/',
         Myprofile.as_view(),
         name="moviesystem_logged_in_profile_urlpattern")

]
